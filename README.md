# Alpha-3.0 (Databázový systém - Kybernetická bezpečnost)
## Autor: Tomáš Novotný, kontakt: novotny10@spsejecna.cz
## Datum vypracování: 19.01.2024 - 04.02.2024
## Název a adresa školy: Střední průmyslová škola elektrotechnická, Praha 2, Ječná 30

# *Popis programu*
- Alpha-3.0 představuje monolitickou aplikaci pro správu uživatelů, rolí a oprávnění v relační databázi.
- Aplikace je napsána v jazyce Python a využívá knihovny pro uživatelské rozhraní (Tkinter), práci s databází (pyodbc) a manipulaci s daty (csv).
- Program je navržen pro jednoduchou a přehlednou správu uživatelů, rolí, oprávění a operací nad nimi.
</br></br>

# *Databáze*
## *E-R model*
- Konceptuální (logický) model databáze se nachází v /SQL/img/Logical.png
- Relační model databáze se nachází v /SQL/img/Relational.png
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

# *Nastavení konfiguračního souboru pro připojení k databázi*
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

# *Import struktury databáze a dat od zadavatele*
- Nejprve je nutno si vytvořit novou databázi, čistou, bez jakýchkoliv dat.
- Poté je zapotřebí do této databáze nahrát soubor, který se nachází v /sql/structure.sql, který slouží pro nahrání struktury mé databáze.
- Pokud si přejete načíst do databáze testovací data, je nutno nahrát ještě soubor, který se nachází v /sql/data.sql.
- Pro nahrání pohledů je zapotřebí nahrát soubor script.sql, který se nachází v /sql/script.sql.
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
- `Alpha3.0`
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
- `SQL`
   - `/img`: Adresář pro obrázky logického a relačního modelu databáze.
     - Logical.png
     - Relational.png
   - `/sql`: Adresář pro import databázové struktury, dat a scriptu.
     - data.sql
     - script.sql
     - structure.sql
- Odkaz na plnohodnotnou dokumentaci.txt
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
</br></br>

# *Třída Monolithic.py*
Třída `Monolithic` slouží jako jádro aplikace pro správu uživatelů a rolí v databázi. Obsahuje metody pro připojení k databázi, vkládání, aktualizaci a mazání uživatelů, začátek transakce, importování dat z CSV souboru a získání dat z databáze.

## *Metody*
`__init__(self, config_file_path='Conf/config.json')`: Konstruktor inicializuje objekt třídy `Monolithic` a načte konfigurační data z JSON souboru.

`connect(self)`: Metoda pro připojení k databázi na základě konfiguračních dat.

`disconnect(self)`: Metoda pro odpojení od databáze.

`insert_user(self, first_name, last_name, email, password, create_window: CreateWindow)`: Metoda pro vložení nového uživatele do databáze a přiřazení role.

`update_user(self, crud_window: CRUDWindow)`: Metoda pro aktualizaci uživatele v databázi a přiřazení role.

`delete_user(self, crud_window: CRUDWindow)`: Metoda pro smazání uživatele z databáze a případně i jeho role.

`begin_transaction(self)`: Metoda pro zahájení nové transakce pro vložení nového uživatele a přiřazení role.

`fetch_data(self)`: Získání dat z databáze -> List obsahující všechny záznamy z pohledu (View) `UserLogsView`.

`import_csv(self)`: Importování dat z CSV souboru do databáze.
   ## *Jak vložit data ze souboru CSV*
   - Pro správný import dat ze souboru CSV je zapotřebí znát následující body:
     1. Data ze souboru se vloží do tabulek `Users` a `Roles`.
     2. Při vkládání nového uživatele je důležité napsat nejdříve křestní jméno uživetele, poté znak `,` a poté bez mezery pokračovat příjmením, následně znovu znak `,` a znovu pokračovat bez mezery e-mailem, nakonec znovu pokračovat znakem `,` a poté znovu bez mezery pokračovat heslem uživatele.
     3. Pokud si přejete vložit více uživatelů najednou, tak každého nového uživatele napište hned pod řádek předchozího uživatele.
     4. Když budete chtít vložit nové role, tak udělejte volný řádek pod uživateli, tím separujete jaká data se mají vložit do tabulky `Users` a jaká do tabulky `Roles`.
     5. Při vkládání nové role je důležité napsat nejříve název role, poté znak `,` a poté bez mezery pokračovat popisem dané role.
     ### *Příklad správně napsaného CSV souboru připraveného k importu do databáze*
     ```csv
       John,Doe,john.doe@exampasdle.com,password123
       Jane,Smith,jane.smith@exdsfample.com,securepass

       Admin,Administrator with full access
       User,Regular user with limited access
     ```
