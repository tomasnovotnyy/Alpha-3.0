import tkinter as tk


class ConnectWindow:
    """
    Třída ConnectWindow reprezentuje okno pro připojení k databázi.
    """

    def __init__(self, root, return_callback, monolothic, update_connection_callback, update_disconnection_callback):
        """
        Inicializace objektu třídy ConnectWindow.
        :param root: Hlavní okno aplikace
        :param return_callback: Callback pro návrat do předchozího okna
        :param monolothic: Instance třídy Monolithic pro manipulaci s databází
        :param update_connection_callback: Callback pro aktualizaci stavu připojení
        :param update_disconnection_callback: Callback pro aktualizaci stavu odpojení
        """
        self.root = root
        self.return_callback = return_callback
        self.monolithic = monolothic
        self.update_connection_callback = update_connection_callback
        self.update_disconnection_callback = update_disconnection_callback

        # Vytvoření nového okna
        self.window = tk.Toplevel(self.root)
        self.window.geometry(self.root.geometry())
        self.window.title("Connect Window")

        # Vytvoření labelu pro nadpis
        top_label = tk.Label(self.window, text="Connect Window")
        top_label.config(font=("Arial", 20))
        top_label.pack(pady=20)

        # Tlačítko pro připojení k databázi
        self.connect_button = tk.Button(self.window, text="Connect", command=self.connect_to_database, width=15)
        self.connect_button.pack(pady=25)
        # Pokud je již připojeno, tlačítko pro připojení bude neaktivní
        if self.monolithic.connected:
            self.connect_button.config(state="disabled")
        else:
            self.connect_button.config(state="normal")

        # Tlačítko pro odpojení od databáze
        self.disconnect_button = tk.Button(self.window, text="Disconnect", command=self.disconnect_from_database,
                                           width=15)
        self.disconnect_button.pack(pady=10)
        # Pokud není připojeno, tlačítko pro odpojení bude neaktivní
        if not self.monolithic.connected:
            self.disconnect_button.config(state="disabled")
        else:
            self.disconnect_button.config(state="normal")

        # Label pro zobrazení stavu připojení
        self.connection_status_label = tk.Label(self.window, text="Not connected", fg="red")
        self.connection_status_label.pack(pady=20)

        # Tlačítko pro návrat do předchozího okna
        return_button = tk.Button(self.window, text="Return", command=self.return_to_previous, width=15)
        return_button.pack(pady=25)

        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        # Aktualizace stavu připojení při inicializaci okna
        self.update_connection_status()

    def return_to_previous(self):
        """
        Metoda pro návrat do předchozího okna.
        """
        self.window.destroy()
        if self.return_callback:
            self.return_callback()

    def connect_to_database(self):
        """
        Metoda pro připojení k databázi.
        """
        self.monolithic.connect()
        if self.monolithic.connected:
            self.update_connection_status()
            if self.update_connection_callback:
                self.update_connection_callback()
            self.return_to_previous()

    def disconnect_from_database(self):
        """
        Metoda pro odpojení od databáze.
        """
        self.monolithic.disconnect()
        self.update_connection_status()
        if self.update_disconnection_callback:
            self.update_disconnection_callback()
        self.disconnect_button.config(state="disabled")
        self.connect_button.config(state="normal")
        self.return_to_previous()

    def update_connection_status(self):
        """
        Metoda pro aktualizaci zobrazení stavu připojení.
        """
        if self.monolithic.connected:
            self.connection_status_label.config(text="Connected", fg="green")
        else:
            self.connection_status_label.config(text="Not connected", fg="red")

    def on_close(self):
        """
        Metoda pro zavření okna a zachycení zavíracího signálu.
        """
        self.window.destroy()
        if self.return_callback:
            self.return_callback()
