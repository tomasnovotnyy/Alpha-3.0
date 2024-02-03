import tkinter as tk
from src.UI.CreateWindow import CreateWindow


class CRUDWindow:
    """
    Třída CRUDWindow reperezentuje okno pro vytvoření, úpravu a smazání uživatele.
    """

    def __init__(self, root, return_callback, monolithic, connect_window):
        """
        Inicializace objektu třídy CRUDWindow.
        :param root: Hlavni okno aplikace
        :param return_callback: Callback pro návrat na předchozí okno
        :param monolithic: Instance třídy Monolithic pro manipulaci s databází
        :param connect_window: Instance třídy ConnectWindow pro připojení k databázi
        """
        self.root = root
        self.return_callback = return_callback
        self.monolithic = monolithic
        self.connect_window = connect_window

        self.window = tk.Toplevel(self.root)
        self.window.geometry(self.root.geometry())
        self.window.title("CRUD Window")

        top_label = tk.Label(self.window, text="CRUD Window")
        top_label.config(font=("Arial", 20))
        top_label.pack(pady=20)

        create_button = tk.Button(self.window, text="CREATE", command=self.create_action, width=15)
        create_button.pack(pady=25)

        alter_button = tk.Button(self.window, text="ALTER", command=self.alter_action, width=15)
        alter_button.pack(pady=25)

        delete_button = tk.Button(self.window, text="DELETE", command=self.delete_action, width=15)
        delete_button.pack(pady=25)

        self.return_button = tk.Button(self.window, text="Return", command=self.return_to_previous, width=15)
        self.return_button.pack(pady=25)

        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", lambda: None)

    def return_to_previous(self):
        """
        Metoda pro návrat do předchozího okna.
        """
        self.window.destroy()
        if self.return_callback:
            self.return_callback()

    def create_action(self):
        """
        Metoda pro vytvoření nového okna pro vytvoření uživatele.
        """
        self.create_window = CreateWindow(self.root, self.monolithic, self.return_to_previous)
        self.window.withdraw()

    def alter_action(self):
        """
        Metoda pro úpravu existujícího uživatele.
        """
        self.monolithic.update_user(self)

    def disable_return_button(self):
        """
        Metoda pro deaktivaci tlačítka pro návrat.
        """
        self.return_button.config(state="disabled")

    def enable_return_button(self):
        """
        Metoda pro aktivaci tlačítka pro návrat.
        """
        self.return_button.config(state="normal")

    def delete_action(self):
        """
        Metoda pro smazání existujícího uživatele.
        """
        self.monolithic.delete_user(self)
