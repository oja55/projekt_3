# Elections Scraper

# Popis projektu

Tento script slouží ke stahování výsledků z parlamentních voleb v roce 2017. Odkaz: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ

# Instalace knihoven

Všechny knihovny jsou uložené v souboru requirements.txt. Pro instalaci v PyCharmu klikněte na Python Interpreter v "settings" a pomocí znaménka "+" nainstalujte potřebné knihovny.

# Spuštení projektu

Spuštění projektu je přes terminál a bude vyžadovat 2 argumenty. Do prvního se zadá url ze sloupce "výběr obce" (označeno "X") a druhý argument je výsledné pojmenování souboru ve kterém se tabulka uloží. Musí končit příponou ".csv".

# Ukázka projektu

Výsledky hlasování pro Most:

    1. argument: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4205
    2. argument: vysledky_most.csv

Spuštění programu:

    PS C:\Users\Ondřej\PycharmProjects\projekt_3 Engeto> python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4205" vysledky_most.csv

Průběh stahování:

    Downloading...
    Download complete. Saved file: vysledky_most.csv

Částečný výstup:

![csv most](https://user-images.githubusercontent.com/116887934/217022028-00816778-dfb4-4ec9-bc93-9c117304696e.png)

