import csv
import json
import random
import re
from tkinter import messagebox, ttk, filedialog, simpledialog
import pyodbc  # pip install pyodbc
import tkinter as tk
from src.UI.CRUDWindow import CRUDWindow
from src.UI.CreateWindow import CreateWindow


class Monolithic:
    """
    Třída Monolithic obsahuje metody pro připojení k databázi, vkládání, aktualizaci a mazání uživatelů,
    začátek transakce, importování dat z CSV souboru a získání dat z databáze.
    """

    def __init__(self, config_file_path='Conf/config.json'):
        """
        Inicializuje objekt třídy Monolithic a načte konfigurační data z JSON souboru.
        :param config_file_path: Cesta k JSON souboru s konfiguračnímí daty.
        """
        with open(config_file_path, 'r') as config_file:
            config_data = json.load(config_file)

        self.SERVER = config_data["database_config"]["SERVER"]
        self.DATABASE = config_data["database_config"]["DATABASE"]
        self.UID = config_data["database_config"]["UID"]
        self.PWD = config_data["database_config"]["PWD"]
        self.connection = None
        self.connected = False

    def connect(self):
        """
        Připojení uživatele k databázi na základě konfiguračních dat.
        """
        try:
            connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.SERVER};DATABASE={self.DATABASE};UID={self.UID};PWD={self.PWD}'
            self.connection = pyodbc.connect(connection_string)
            messagebox.showinfo("Success", "Connected to the database.")
            self.connected = True
        except (pyodbc.InterfaceError, pyodbc.OperationalError) as e:
            messagebox.showerror("Error", "Error connecting to the database: Invalid server details or credentials.")
        except Exception as e:
            messagebox.showerror("Error", f"Error connecting to the database: {str(e)}")

    def disconnect(self):
        """
        Odpojení uživatele od databáze.
        """
        self.connection.close()
        self.connected = False
        messagebox.showinfo("Success", "Disconnected from the database.")

    def insert_user(self, first_name, last_name, email, password, create_window: CreateWindow):
        """
        Vložení nového uživatele do databáze.
        :param first_name: Křestní jméno uživatele.
        :param last_name: Příjmení uživatele.
        :param email: Email uživatele.
        :param password: Heslo uživatele.
        :param create_window: Instance třídy CreateWindow -> okno pro vytvoření uživatele.
        """
        try:
            cursor = self.connection.cursor()
            insert_query = (f"INSERT INTO Users (First_name, Last_name, Email, Password) OUTPUT INSERTED.ID VALUES (?, "
                            f"?, ?, ?)")
            last_inserted_id = cursor.execute(insert_query, (first_name, last_name, email, password)).fetchone()[0]
            self.connection.commit()

            # Zapisování do tabulky Logs
            log_query = "INSERT INTO Logs (Users_ID, Action, Status) VALUES (?, 'User created', 'Success')"
            cursor.execute(log_query, (last_inserted_id,))
            self.connection.commit()

            create_window.disable_return_button()
            messagebox.showinfo("Action", "User created.")

            # Získání rolí z tabulky Roles
            cursor.execute("SELECT * FROM Roles")
            roles = cursor.fetchall()

            # Kontrola, zda jsou role k dispozici
            if not roles:
                messagebox.showinfo("Action", "No roles to assign.")
                create_window.enable_return_button()
                return

            # Vytvoření nového okna pro přiřazení role
            role_window = tk.Toplevel()
            role_window.title("Role Assignment")
            role_window.resizable(False, False)

            # Zakázání tlačítka pro zavření okna
            role_window.protocol("WM_DELETE_WINDOW", lambda: None)

            role_var = tk.StringVar()
            role_var.set('Select a role')

            # Použití Comboboxu pro výběr role
            role_combobox = ttk.Combobox(role_window, textvariable=role_var, values=[role[1] for role in roles],
                                         state="readonly")
            role_combobox.pack(pady=10)

            def on_submit():
                chosen_role = role_var.get()
                chosen_role_id = next((role[0] for role in roles if role[1] == chosen_role),
                                      None)

                if chosen_role_id is not None:
                    submit_button.config(state=tk.DISABLED)
                    role_combobox.config(state=tk.DISABLED)
                    cursor.execute("INSERT INTO UserRoles (Users_ID, Roles_ID) VALUES (?, ?)",
                                   (last_inserted_id, chosen_role_id))
                    self.connection.commit()
                    messagebox.showinfo("Action", "Role assigned.")
                    role_window.destroy()
                    create_window.enable_return_button()

            submit_button = tk.Button(role_window, text="Submit", command=on_submit)
            submit_button.pack()
        except pyodbc.IntegrityError:
            messagebox.showerror("Error", "User with this email already exists or your email is in a wrong format.")

    def update_user(self, crud_window: CRUDWindow):
        """
        Aktualizace uživatele v databázi.
        :param crud_window: Instance třídy CRUDWindow -> okno pro aktualizaci uživatele.
        """
        try:
            crud_window.disable_return_button()
            # Vytvoření dialogového okna pro zadání emailu
            email = simpledialog.askstring("Input", "Enter the email of the user you want to alter:")

            cursor = self.connection.cursor()

            # Kontrola, zda email existuje v databázi
            cursor.execute("SELECT ID FROM Users WHERE Email = ?", (email,))
            user_id = cursor.fetchone()

            if user_id is None:
                crud_window.enable_return_button()
                raise Exception("No user found with the provided email.")

            cursor.execute("SELECT * FROM Roles")
            roles = cursor.fetchall()

            role_window = tk.Toplevel()
            role_window.title("Role Assignment")
            role_window.resizable(False, False)

            # Zakázání tlačítka pro zavření okna
            role_window.protocol("WM_DELETE_WINDOW", lambda: None)

            role_var = tk.StringVar()
            role_var.set('Select a role')

            # Použití Comboboxu pro výběr role
            role_combobox = ttk.Combobox(role_window, textvariable=role_var, values=[role[1] for role in roles],
                                         state="readonly")
            role_combobox.pack(pady=10)

            def on_submit():
                chosen_role = role_var.get()
                chosen_role_id = next((role[0] for role in roles if role[1] == chosen_role),
                                      None)

                if chosen_role_id is not None:
                    submit_button.config(state=tk.DISABLED)
                    role_combobox.config(state=tk.DISABLED)
                    # Kontrola, zda uživatel má přiřazenou roli
                    cursor.execute("SELECT * FROM UserRoles WHERE Users_ID = ?", (user_id[0],))
                    user_role = cursor.fetchone()

                    if user_role is None:
                        cursor.execute("INSERT INTO UserRoles (Users_ID, Roles_ID) VALUES (?, ?)",
                                       (user_id[0], chosen_role_id))
                        messagebox.showinfo("Action", "Role assigned.")
                        # Zápis do tabulky Logs
                        cursor.execute(
                            "INSERT INTO Logs (Users_ID, Action, Status) VALUES (?, 'Role assigned', 'Success')",
                            (user_id[0],))
                    else:
                        # Aktualizace role uživatele
                        cursor.execute("UPDATE UserRoles SET Roles_ID = ? WHERE Users_ID = ?",
                                       (chosen_role_id, user_id[0]))
                        messagebox.showinfo("Action", "Role updated.")
                        # Zápis do tabulky Logs
                        cursor.execute(
                            "INSERT INTO Logs (Users_ID, Action, Status) VALUES (?, 'Role updated', 'Success')",
                            (user_id[0],))

                    self.connection.commit()
                    role_window.destroy()
                    crud_window.enable_return_button()

            submit_button = tk.Button(role_window, text="Submit", command=on_submit)
            submit_button.pack()
        except Exception as e:
            messagebox.showerror("Error", f"{str(e)}")
            self.connection.rollback()

    def delete_user(self, crud_window: CRUDWindow):
        """
        Smazání uživatele z databáze.
        :param crud_window: Instance třídy CRUDWindow -> okno pro smazání uživatele.
        """
        try:
            crud_window.disable_return_button()
            # Vytvoření dialogového okna pro zadání emailu
            email = simpledialog.askstring("Input", "Enter the email of the user you want to delete:")

            cursor = self.connection.cursor()

            # Kontrola, zda email existuje v databázi
            cursor.execute("SELECT ID FROM Users WHERE Email = ?", (email,))
            user_id = cursor.fetchone()

            if user_id is None:
                crud_window.enable_return_button()
                raise Exception("No user found with the provided email.")

            # Kontrola, zda uživatel má přiřazenou roli
            cursor.execute("SELECT * FROM UserRoles WHERE Users_ID = ?", (user_id[0],))
            user_role = cursor.fetchone()

            if user_role is not None:
                # Smazání role uživatele
                cursor.execute("DELETE FROM UserRoles WHERE Users_ID = ?", (user_id[0],))
                # Zápis do tabulky Logs
                cursor.execute("INSERT INTO Logs (Users_ID, Action, Status) VALUES (?, 'User role deleted', 'Success')",
                               (user_id[0],))

            cursor.execute("INSERT INTO Logs (Users_ID, Action, Status) VALUES (?, 'User deleted', 'Success')",
                           (user_id[0],))

            # Smazání uživatele z tabulky Logs
            cursor.execute("DELETE FROM Logs WHERE Users_ID = ?", (user_id[0],))

            # Smazání uživatele z tabulky Users
            cursor.execute("DELETE FROM Users WHERE ID = ?", (user_id[0],))

            self.connection.commit()
            messagebox.showinfo("Action", "User deleted.")
            crud_window.enable_return_button()
        except Exception as e:
            messagebox.showerror("Error", f"{str(e)}")
            self.connection.rollback()

    def begin_transaction(self):
        """
        Zahájení nové transakce pro vložení nového uživatele a přiřazení role.
        """
        try:
            # Začátek transakce
            cursor = self.connection.cursor()

            # Vložení nového uživatele
            insert_query = (f"INSERT INTO Users (First_name, Last_name, Email, Password) OUTPUT INSERTED.ID VALUES (?, "
                            f"?, ?, ?)")
            new_user = ('John', 'Doe', 'john.doe@example2.com', 'password')

            # Kontrola, zda email uživatele již existuje v databázi
            cursor.execute("SELECT Email FROM Users WHERE Email = ?", (new_user[2],))
            existing_email = cursor.fetchone()
            if existing_email is not None:
                raise Exception(f"User with email {new_user[2]} already exists.")

            last_inserted_id = cursor.execute(insert_query, new_user).fetchone()[0]

            cursor.execute("SELECT ID FROM Roles")
            role_ids = [row[0] for row in cursor.fetchall()]

            if role_ids:
                # Náhodný výběr role
                role_id = random.choice(role_ids)

                # Přiřazení role uživateli
                cursor.execute("INSERT INTO UserRoles (Users_ID, Roles_ID) VALUES (?, ?)",
                               (last_inserted_id, role_id))

                # Zápis do tabulky Logs
                cursor.execute(
                    "INSERT INTO Logs (Users_ID, Action, Status) VALUES (?, 'User registration - TRANSACTION', "
                    "'Success')",
                    (last_inserted_id,))

                self.connection.commit()

                messagebox.showinfo("Action", "User registered and role assigned.\nTransaction action committed.")
            else:
                raise Exception("No roles found in the Roles table.")
        except Exception as e:
            self.connection.rollback()
            messagebox.showerror("Error", f"Error registering user and assigning role: {str(e)}")

    def fetch_data(self):
        """
        Načtení dat z databáze.
        :return: Vrací všechny záznamy z pohledu (View) UserLogsView.
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM UserRolesView")
        return cursor.fetchall()

    def import_csv(self):
        """
        Importování dat z CSV souboru do databáze.
        """
        global cursor
        try:
            messagebox.showinfo("Import", "Choose a CSV file to import.")
            file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

            if not file_path:
                raise Exception("No file selected.")
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                data = [tuple(row) for row in reader]

            blank_line_index = data.index(())
            user_data = data[:blank_line_index]
            role_data = data[blank_line_index + 1:]

            cursor = self.connection.cursor()
            insert_query_users = "INSERT INTO Users (First_name, Last_name, Email, Password) VALUES (?, ?, ?, ?)"
            insert_query_roles = "INSERT INTO Roles (Role_name, Role_description) VALUES (?, ?)"

            email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

            cursor.execute("BEGIN TRANSACTION")

            for row in user_data:
                if not email_regex.match(row[2]):
                    raise Exception(f"Invalid email format: {row[2]}")

                # Kontrola existence emailu v databázi
                cursor.execute("SELECT Email FROM Users WHERE Email = ?", (row[2],))
                existing_email = cursor.fetchone()
                if existing_email is not None:
                    raise Exception(f"Email already exists in the database: {row[2]}")

                cursor.execute(insert_query_users, row)
                last_inserted_id = cursor.execute("SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                log_query = (
                    f"INSERT INTO Logs (Users_ID, Action, Status) VALUES (?, 'User imported from CSV file', 'Success')")
                cursor.execute(log_query, (last_inserted_id,))

            for row in role_data:
                # Kontrola existence role v databázi
                cursor.execute("SELECT Role_name FROM Roles WHERE Role_name = ?",
                               (row[0],))
                existing_role = cursor.fetchone()
                if existing_role is not None:
                    raise Exception(f"Role already exists in the database: {row[0]}")
                cursor.execute(insert_query_roles, row)
            cursor.execute("COMMIT TRANSACTION")
            self.connection.commit()

            messagebox.showinfo("Import", "Data imported successfully.")
        except Exception as e:
            cursor.execute("ROLLBACK TRANSACTION")
            self.connection.rollback()
            messagebox.showerror("Error", f"{str(e)}")
