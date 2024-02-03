import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime


class ReportWindow:
    """
    Třída ReportWindow slouží pro zostavení okna s reportem.
    """

    def __init__(self, root, return_callback, monolithic):
        """
        Inicializace objektu třídy ReportWindow.
        :param root: Hlavni okno aplikace
        :param return_callback: Callback pro návrat do předchozího okna
        :param monolithic: Inistance třídy Monolithic pro manipulaci s databází
        """
        self.root = root
        self.return_callback = return_callback
        self.monolithic = monolithic

        data = self.monolithic.fetch_data()

        self.window = tk.Toplevel(self.root)
        self.window.title("Report Window")
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        self.tree = ttk.Treeview(self.window, height=len(data))
        self.tree['columns'] = ('#1', '#2', '#3', '#4', '#5', '#6', '#7')
        self.tree.column('#1', width=50)
        self.tree.column('#2', width=75)
        self.tree.column('#3', width=80)
        self.tree.column('#4', width=175)
        self.tree.column('#5', width=75)
        self.tree.column('#6', width=190)
        self.tree.column('#7', width=55)
        self.tree.heading('#1', text='User_ID')
        self.tree.heading('#2', text='First_name')
        self.tree.heading('#3', text='Last_name')
        self.tree.heading('#4', text='Email')
        self.tree.heading('#5', text='Role_name')
        self.tree.heading('#6', text='Action')
        self.tree.heading('#7', text='Status')
        self.tree['show'] = 'headings'
        self.tree.grid()

        self.tree.bind("<Button-1>", self.check_resize)

        for row in data:
            formatted_row = []
            for value in row:
                if isinstance(value, datetime):
                    formatted_value = value.strftime("%d.%m.%Y %H:%M:%S")
                else:
                    formatted_value = value
                formatted_row.append(formatted_value)
            self.tree.insert("", "end", values=formatted_row)

        self.window.update_idletasks()
        self.window.geometry(f'{self.tree.winfo_width()}x{self.tree.winfo_height()}')

    def on_close(self):
        """
        Metoda pro zavření okna a zachycení zavíracího signálu.
        """
        self.window.destroy()
        if self.return_callback:
            self.return_callback()

    def check_resize(self, event):
        """
        Metoda pro kontrolu změny velikosti okna.
        :param event: Událost změny velikosti okna
        """
        region = self.tree.identify_region(event.x, event.y)

        if region == 'separator':
            return "break"
