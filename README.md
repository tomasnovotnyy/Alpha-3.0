# Alpha-3.0 (Databázový systém - Kybernetická bezpečnost)
## Autor: Tomáš Novotný, kontakt: XXXXXXXXXXX
## Datum vypracování: 19.01.2024 - 04.02.2024
## Název a adresa školy: Střední průmyslová škola elektrotechnická, Praha 2, Ječná 30

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
</br></br>

# Nastavení konfiguračního souboru pro připojení k databázi
Před spuštěním programu je nutné nastavit konfigurační soubor, který obsahuje informace o připojení k databázi. Níže jsou uvedeny kroky, které je třeba provést:
- **Nastavte hodnoty v konfiguračním souboru**
   - Otevřete `config.json`, který se nachází ve složce `/Conf`, ve svém oblíbeném textovém editoru a nastavte následující hodnoty podle vašich potřeb:
   ```json
   {
     "database_config": {
       "SERVER": "NÁZEV_SERVERU",
       "DATABASE": "NÁZEV_DATABÁZE",
       "UID": "UŽIVATELSKÉ_ID",
       "PWD": "HESLO"
     }
   }

</br></br>

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

# *Struktura projektu*
- `/Conf`: Adresář pro konfigurační soubor.
  - config.json
- `/Doc`: Adresář pro dokumentaci.
  - README.md
- `/Log`: Adresář pro logování chyb a událostí.
  - ErrorFileLog.txt
- `/src`: Adresář obsahující třídy pro funkcionalitu aplikace.
  - `/DB`
    - Monolithic.py
  - `/UI`
    - ConnectWindow.py
    - CreateWindow.py
    - CRUDWindow.py
    - ImportWindow.py
    - ReportWindow.py
    - UI.py
- Main.py
</br></br>

# *Funkce a Možnosti*
1. Připojení a Odpojení od Databáze
   - Uživatel se může připojit k databázi pomocí konfiguračního souboru (config.json) a následně se může i ručně odpojit.
2. Správa uživatelů
   - Vytváření nových uživatelů s přidělením rolí.
   - Aktualizace rolí existujících uživatelů.
   - Odstranění uživatelů z databáze.
3. Transakce
   - Demonstrace transakční operace, která registruje nového uživatele a přiřazuje mu roli.
4. Import dat z CSV
   - Import uživatelů a rolí z CSV souboru do databáze.
5. Získání Dat (Report)
   - Získání dat z databázového pohledu (UserLogsView) pro report uživatelských operací.
