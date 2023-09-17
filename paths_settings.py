import pathlib
import csv
import json
import sys

PATH: str = str(pathlib.Path(sys.executable).parent)
PATH: str = str(pathlib.Path(pathlib.Path(__file__).parent)) # Comment out this line when converting to exe

ICON_PATH : str = str(pathlib.Path(PATH, "icon.png"))
BANNER_PATH : str = str(pathlib.Path(PATH, "banner.png"))

langs = {"PL": 0,
         "EN": 1}

with open(file= str(pathlib.Path(PATH, "settings.json")),
          mode= "r",
          encoding= "UTF-8") as file:
    read = json.load(file)
    lang = langs[read['language']]


with open(file= str(pathlib.Path(PATH, "languages.csv")), 
          mode= "r",
          encoding= "UTF-8") as file:
    reader = csv.reader(file)

    for nr, row in enumerate(reader):
        row= row[lang]
        if nr == 0:
            CHOOSE_FILE = row
        elif nr == 1:
            CHOOSE_CORRECT_FILE = row
        elif nr == 2:
            FILTER_TXT = row
        elif nr == 3:
            FILTER_ALL = row
        elif nr == 4:
            SOURCE_CODE = row
        elif nr == 5:
            TIME_DELTA = row
        elif nr == 6:
            TAGGING = row
        elif nr == 7:
            START = row