import tkinter as tk


class ImportWindow:
    """
    Třída ImportWindow reprezentuje okno pro import dat z CSV souboru.
    """

    def __init__(self, root, monolithic):
        """
        Inicializace objektu třídy ImportWindow.
        :param root: Hlavni okno aplikace.
        :param monolithic: Instance třídy Monolithic pro manipulaci s databází.
        """
        self.root = root
        self.monolithic = monolithic
        self.import_button = tk.Button(self.root, text="Import CSV", command=self.import_csv, width=15)

    def import_csv(self):
        """
        Metoda pro import dat z CSV souboru do databáze.
        """
        self.monolithic.import_csv()
