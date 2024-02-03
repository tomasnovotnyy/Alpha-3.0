import tkinter as tk
from tkinter import messagebox
from src.DB.Monolithic import Monolithic
from src.UI.CRUDWindow import CRUDWindow
from src.UI.ConnectWindow import ConnectWindow
from src.UI.ReportWindow import ReportWindow
from src.UI.ImportWindow import ImportWindow


class UI:
    """
    Třída UI reprezentuje uživatelské rozhraní mé aplikace Alpha 3.0.
    """

    def __init__(self, root):
        """
        Inicializace objektu třídy UI.
        :param root: Hlavní okno aplikace.
        """

        # Nastavení proměnných
        self.db_connection = None
        self.monolithic = Monolithic()
        self.current_window = None
        self.root = root
        self.root.title("Alpha 3.0")

        # Nastavení titulku
        self.title_label = tk.Label(self.root, text="Alpha 3.0")
        self.title_label.config(font=("Arial", 20))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=30, sticky="n")

        # Nastavení tlačítek pro CRUD operace
        self.crud_button = tk.Button(self.root, text="CRUD", command=self.open_crud_window, width=15)
        self.crud_button.grid(row=1, column=0, pady=25, sticky="n")
        if not self.monolithic.connected:
            self.crud_button.config(state="disabled")
        else:
            self.crud_button.config(state="normal")

        # Nastavení transakčního tlačítka
        self.transaction_button = tk.Button(self.root, text="TRANSACTION", command=self.begin_transaction, width=15)
        self.transaction_button.grid(row=1, column=1, pady=25, sticky="n")
        if not self.monolithic.connected:
            self.transaction_button.config(state="disabled")
        else:
            self.transaction_button.config(state="normal")

        # Nastavení tlačítka pro report
        self.report_button = tk.Button(self.root, text="REPORT", command=self.open_report_window, width=15)
        self.report_button.grid(row=2, column=0, pady=25, sticky="n")
        if not self.monolithic.connected:
            self.report_button.config(state="disabled")
        else:
            self.report_button.config(state="normal")

        # Nastavení tlačítka pro import
        self.import_button = tk.Button(self.root, text="IMPORT", command=self.open_import_window, width=15)
        self.import_button.grid(row=2, column=1, pady=25, sticky="n")
        if not self.monolithic.connected:
            self.import_button.config(state="disabled")
        else:
            self.import_button.config(state="normal")

        # Nastavení tlačítka pro připojení
        self.connect_button = tk.Button(self.root, text="CONNECTION", command=self.open_connection_window, width=15)
        self.connect_button.grid(row=3, column=0, columnspan=2, pady=25, sticky="n")

        # Nastavení šířky a výšky okna
        self.root.geometry("500x400")
        # Nastavení nezměnitelnosti velikosti okna
        self.root.resizable(False, False)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Nastavení vlastností sloupců a řádků pro umístění na střed
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)

    def open_connection_window(self):
        """
        Metoda pro otevření nového okna pro připojení k databázi.
        """
        self.current_window = ConnectWindow(self.root, self.return_to_previous, self.monolithic,
                                            self.update_ui_after_connection, self.update_ui_after_disconnection)

        # Skrytí hlavního okna
        self.root.withdraw()

    def update_ui_after_connection(self):
        """
        Metoda pro aktualizaci UI po úspěšném připojení k databázi.
        """
        for button in [self.crud_button, self.transaction_button, self.report_button, self.import_button]:
            button.config(state="normal")

    def update_ui_after_disconnection(self):
        """
        Metoda pro aktualizaci UI po úspěšném odpojení od databáze.
        """
        for button in [self.crud_button, self.transaction_button, self.report_button, self.import_button]:
            button.config(state="disabled")

    def open_crud_window(self):
        """
        Metoda pro otevření nového okna pro CRUD operace.
        """
        self.current_window = CRUDWindow(self.root, self.return_to_previous, self.monolithic, self.current_window)
        self.root.withdraw()

    def open_report_window(self):
        """
        Metoda pro otevření nového okna pro zobrazení reportu.
        """
        data = self.monolithic.fetch_data()
        # Pokud nejsou žádná data k zobrazení v pohledu (View), zobrazí se chybová hláška
        if not data:
            messagebox.showerror("Error", "No data to display. Insert some data first.")
            return
        self.current_window = ReportWindow(self.root, self.return_to_previous, self.monolithic)
        self.root.withdraw()

    def open_import_window(self):
        """
        Metoda pro otevření nového okna pro import dat z CSV souboru.
        """
        import_window = ImportWindow(self.root, self.monolithic)
        import_window.import_csv()

    def begin_transaction(self):
        """
        Metoda pro zahájení transakce.
        """
        self.monolithic.begin_transaction()

    def return_to_previous(self):
        """
        Metoda pro návrat do předchozího okna.
        """
        if self.current_window:
            self.current_window.window.destroy()
            self.current_window = None

        # Odebrání skrytého stavu hlavního okna a jeho opětovné zobrazení
        self.root.deiconify()

    def on_close(self):
        """
        Metoda pro zavření okna a zachycení zavíracího signálu.
        """
        if self.monolithic.connected:
            self.monolithic.disconnect()

        self.root.destroy()
