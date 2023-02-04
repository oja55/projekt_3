"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Ondřej Vítek
email: ondra5510@gmail.com
discord: oja55#8858
"""

import sys
import csv
from bs4 import BeautifulSoup
import requests


def check_arguments():
    if len(sys.argv) != 3:
        print("Program need 2 arguments, shutting down the program...")
        exit()
    elif not sys.argv[1].startswith("https://www.volby.cz/pls/ps2017nss/"):
        print("Wrong url, shutting down the program...")
        exit()
    elif not sys.argv[2].endswith(".csv"):
        print("Must be .csv file, shutting down the program.")
        exit()
    else:
        csv_output()
        print(f"Download complete. Saved file: {sys.argv[2]}")


def get_url():
    base_url = sys.argv[1]
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def get_town_codes():
    code_elements = get_url().find_all("td", {"class": "cislo"})
    codes = [code.get_text() for code in code_elements]
    return codes


def get_town_names():
    town_elements = get_url().find_all("td", {"class": "overflow_name"})
    town_names = [town.get_text() for town in town_elements]
    return town_names


def get_codes_url():
    url_towns = get_url().find_all("td", {"class": "cislo"})
    url_list = []
    for url in url_towns:
        url_list.append(url.find("a")["href"])
    sub_url = ["https://volby.cz/pls/ps2017nss/" + url_list[i] for i in range(len(url_list))]
    return sub_url


def sub_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def get_registered():
    register_list = []
    for url in get_codes_url():
        registered_elements = sub_url(url).find_all("td", {"class": "cislo"}, headers="sa2")
        registered_list = [registered.get_text().replace("\xa0", "") for registered in registered_elements]
        register_list.extend(list(map(int, registered_list)))
    return register_list



def get_envelopes():
    envelop_list = []
    for url in get_codes_url():
        envelopes_elements = sub_url(url).find_all("td", {"class": "cislo"}, headers="sa3")
        envelopes_list = [envelopes.get_text().replace("\xa0", "") for envelopes in envelopes_elements]
        envelop_list.extend(list(map(int, envelopes_list)))
    return envelop_list


def get_valid_votes():
    validate_list = []
    for url in get_codes_url():
        valid_elements = sub_url(url).find_all("td", {"class": "cislo"}, headers="sa6")
        valid_list = [valid.get_text().replace("\xa0", "") for valid in valid_elements]
        validate_list.extend(list(map(int, valid_list)))
    return validate_list


def sub_url_partis():
    response = requests.get(get_codes_url()[0])
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def get_party():
    party_elements = sub_url_partis().find_all("td", {"class": "overflow_name"})
    party_names = [party.get_text() for party in party_elements]
    return party_names


def get_votes():
    votes_list = []
    for url in get_codes_url():
        votes_elements = sub_url(url).find_all("td", {"class": "cislo"}, headers=["t1sb3", "t2sb3"])
        get_votes = [votes.get_text().replace("\xa0", "") for votes in votes_elements]
        votes_list.append(list(map(int, get_votes)))
    return votes_list


def csv_output():
    print("Downloading...")
    header = ["code", "location", "registered", "envelopes", "valid"] + get_party()

    with open(sys.argv[2], "w", newline="") as file:
         writer = csv.writer(file)
         writer.writerow(header)
         for i in range(len(get_town_names())):
             writer.writerow(
                 [get_town_codes()[i],
                  get_town_names()[i],
                  get_registered()[i],
                  get_envelopes()[i],
                  get_valid_votes()[i]
                 ] + get_votes()[i]
              )

if __name__ == "__main__":
    check_arguments()