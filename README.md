# Alpha-3.0 (Databázový systém - Kybernetická bezpečnost)

# *Popis programu*
- Alpha-3.0 představuje monolitickou aplikaci pro správu uživatelů, rolí a oprávnění v relační databázi.
- Aplikace je napsána v jazyce Python a využívá knihovny pro uživatelské rozhraní (Tkinter), práci s databází (pyodbc) a manipulaci s daty (csv).
- Program je navržen pro jednoduchou a přehlednou správu uživatelů, rolí, oprávění a operací nad nimi.
</br></br>

# *Instalace knihovny pyodbc*
- Pro správné fungování programu je zapotřebí doinstalovat knihovnu pyodbc.
## *Varianta pro PyCharm*
- Pokud používáte PyCharm s vlastním venv, stačí si spustit terminál a napsat příkaz:
``` python
pip install pyodbc
```
Nebo můžete použít variantu pro ostatní níže, ale při vytvoření projektu musíte zaškrnout políčko "Inherit global site packages"
## *Varianta VStudio a ostatni*
- Pokud používáte Python bez venv, například pomoci Visual Studio Code, nebo z příkazové řádky použijte v příkazové řádce příkaz:
``` python
pip install --user pyodbc
```
</br>

# *Spuštění programu*
Pro správné spuštění aplikace je třeba mít nainstalovaný Python, knihovnu pyodbc a je zapotřebí spustit skript Main.py z terminálu.</br>
## *Spuštění skriptu Main.py:*
1. Stáhněte si .zip soubor programu do svého PC.
2. Soubor extrahujte. Extrahovaný soubor bude obsahovat 2 následující soubory:
   - Složka Alpha2.0, kde je uložený celý projekt.
   - Textový soubor s odkazem na tuto GitHub stránku a s kontaktem na mě.
4. Spusťte si příkazový řádek.
5. Pomocí příkazu `cd` se dostaňte do složky, kde máte uložený projekt.
6. Pokud jste již uvnitř složky, kde máte uložený projekt, tak program spustíte následujícím příkazem: `python Main.py`

Po úspěšném spuštění skriptu se program inicializuje a zobrazí uživatelské rozhraní, které umožní interakci a využití všech funkcí aplikace.
</br></br>
