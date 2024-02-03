import tkinter as tk
from datetime import datetime
from src.UI.UI import UI


def log_error(error_message):
    """
    Metoda pro zapsání chyby do logu.
    :param error_message: Chybová hláška.
    """
    error_log_path = "Log/ErrorFileLog.txt"
    with open(error_log_path, 'a') as error_file:
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        error_file.write(f"{current_time}: {error_message}\n\n")


# Hlavní část programu
if __name__ == "__main__":
    try:
        """
        Hlavní část programu, která vytvoří instanci uživatelského rozhraní a spustí hlavní smyčku pro zobrazení GUI.
        """
        root = tk.Tk()  # Inicializace hlavního okna Tkinter
        app = UI(root)  # Vytvoření instance uživatelského rozhraní
        root.mainloop()  # Spuštění hlavní smyčky pro zobrazení GUI
    except Exception as e:
        """
        Zachycení chyby, která se může vyskytnout při běhu programu.
        """
        log_error(f"Main Error: {str(e)}")
