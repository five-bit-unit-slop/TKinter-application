# Smart Security met Azure light theme

Een vereenvoudigde versie van de Smart Security Tkinter-app met het Azure light-thema. De code gebruikt gewone functies en variabelen, zonder classes. Het oorspronkelijke README-bestand staat in `ORIGINAL-README.md`.

## Starten

1. Pak het hele archief uit. Houd `main.py`, `azure.tcl` en de map `theme` bij elkaar.
2. Installeer Python 3 met Tkinter. Op sommige Linux-systemen heb je ook `python3-tk` nodig.
3. Open een terminal in de uitgepakte map en voer uit:

   ```bash
   python main.py
   ```

   Gebruik zo nodig `python3 main.py`. Een grafische desktopomgeving is vereist; extra Python-pakketten zijn niet nodig.

## Gebruik

Log in met gebruikersnaam `midas` en wachtwoord `midas735`. Activeer het systeem om een opening van de deur, achterdeur of het achterraam te simuleren. Een gesimuleerde opening blijft open, zoals in het oorspronkelijke prototype.

**Let op:** dit is een prototype. De inloggegevens staan in de broncode; er is geen echte authenticatie of verbinding met beveiligingshardware.

## Herkomst en licentie

- Applicatie: https://github.com/five-bit-unit-slop/TKinter-application, commit `7aef6563430e6690ad3c4ef35653ad74595fc224`.
- Azure ttk theme: https://github.com/rdbende/Azure-ttk-theme, commit `997dbbef09563c3a0b2541ae3de5cd774f1640fb`. Het thema is MIT-gelicentieerd; zie `AZURE-LICENSE.txt`. Beide themamappen zijn meegeleverd omdat `azure.tcl` zowel light als dark inlaadt, maar de applicatie selecteert light.
