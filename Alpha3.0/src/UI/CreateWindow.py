import tkinter as tk
from tkinter import messagebox


class CreateWindow:
    """
    Třída CreateWindow reprezentuje okno pro vytvoření nového uživatele.
    """

    def __init__(self, root, monolithic, return_callback):
        """
        Inicializace okna pro vytvoření nového uživatele.
        :param root: Hlavni okno aplikace
        :param monolithic: Instance třídy Monolithic pro komunikaci a manipulaci s databází
        :param return_callback: Callback pro návrat zpět do předchozího okna
        """
        self.root = root
        self.monolithic = monolithic
        self.return_callback = return_callback

        self.window = tk.Toplevel(self.root)
        self.window.geometry(self.root.geometry())
        self.window.title("Create User")

        top_label = tk.Label(self.window, text="Create User")
        top_label.config(font=("Arial", 20))
        top_label.grid(row=0, column=0, columnspan=2, pady=30, sticky="n")

        first_name_label = tk.Label(self.window, text="First Name")
        first_name_label.grid(row=1, column=0, pady=15, sticky="n")
        self.first_name_entry = tk.Entry(self.window)
        self.first_name_entry.grid(row=1, column=1, pady=15, sticky="n")

        last_name_label = tk.Label(self.window, text="Last Name")
        last_name_label.grid(row=2, column=0, pady=15, sticky="n")
        self.last_name_entry = tk.Entry(self.window)
        self.last_name_entry.grid(row=2, column=1, pady=15, sticky="n")

        email_label = tk.Label(self.window, text="Email")
        email_label.grid(row=3, column=0, pady=15, sticky="n")
        self.email_entry = tk.Entry(self.window)
        self.email_entry.grid(row=3, column=1, pady=15, sticky="n")

        password_label = tk.Label(self.window, text="Password")
        password_label.grid(row=4, column=0, pady=15, sticky="n")
        self.password_entry = tk.Entry(self.window, show="*")
        self.password_entry.grid(row=4, column=1, pady=15, sticky="n")

        create_button = tk.Button(self.window, text="CREATE", command=self.create_action, width=15)
        create_button.grid(row=5, column=0, columnspan=2, pady=15, sticky="n")

        self.return_button = tk.Button(self.window, text="Return", command=self.return_to_previous, width=15)
        self.return_button.grid(row=6, column=0, columnspan=2, pady=15, sticky="n")

        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.disable_close_button())

        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.window.rowconfigure(2, weight=1)
        self.window.rowconfigure(3, weight=1)
        self.window.rowconfigure(4, weight=1)
        self.window.rowconfigure(5, weight=1)
        self.window.rowconfigure(6, weight=1)

    def create_action(self):
        """
        Metoda pro vytvoření nového uživatele.
        """
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not first_name or not last_name or not email or not password:
            messagebox.showerror("Error", "All fields must be filled out.")
            return

        try:
            self.monolithic.insert_user(first_name, last_name, email, password, self)
            self.clear_entries()
        except Exception as e:
            messagebox.showerror("Error CreateWindow", str(e))

    def disable_close_button(self):
        """
        Metoda pro deaktivaci tlačítka pro zavření okna.
        """
        self.window.protocol("WM_DELETE_WINDOW", lambda: None)

    def enable_return_button(self):
        """
        Metoda pro aktivaci tlačítka pro návrat zpět.
        """
        self.return_button.config(state=tk.NORMAL)

    def disable_return_button(self):
        """
        Metoda pro deaktivaci tlačítka pro návrat zpět.
        """
        self.return_button.config(state=tk.DISABLED)

    def clear_entries(self):
        """
        Metoda pro vyčištění vstupních polí.
        """
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def return_to_previous(self):
        """
        Metoda pro návrat zpět do předchozího okna.
        """
        self.window.destroy()
        if self.return_callback:
            self.return_callback()
