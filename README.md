# Elections Scraper

# Popis projektu

Tento script slouží ke stahování výsledků z parlamentních voleb v roce 2017. Odkaz: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ

# Instalace knihoven

Všechny knihovny jsou uložené v souboru requirements.txt. Pro instalaci v PyCharmu klikněte na Python Interpreter v "settings" a pomocí znaménka "+" nainstalujte potřebné knihovny.

# Spuštení projektu

Spuštění projektu je přes terminál a bude vyžadovat 2 argumenty. Do prvního se zadá url ze sloupce "výběr obce" (označeno "X") a druhý argument je výsledné pojmenování souboru ve kterém se tabulka uloží. Musí končit příponou ".csv".

# Ukázka projektu

# Výsledky hlasování pro Plzeň-město:

    1. argument: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=4&xnumnuts=3203
    2. argument: vysledky_plzen.csv

Spuštění programu:

![terminal start](https://user-images.githubusercontent.com/116887934/216806496-c0848bdb-1511-462a-84ac-caef01cace0e.png)

Průběh stahování:

![terminal complete](https://user-images.githubusercontent.com/116887934/216806696-3e108a6c-822d-4e89-b012-8e28a028bf36.png)

Částečný výstup:

![csv output](https://user-images.githubusercontent.com/116887934/216806600-0789bf0a-2528-4e6f-adda-96865a81d08b.png)
