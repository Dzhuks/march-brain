import csv
import os
from datetime import date


DB_PATH = "history.csv"
FIELDNAMES = ['Дата', 'Файл', 'Диагноз']


def _create_db_if_not_exist():
    if os.path.isfile(DB_PATH):
        return
    with open(DB_PATH, 'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=";", fieldnames=FIELDNAMES, lineterminator='\n')
        writer.writeheader()


def add_row(filename, diagnosis):
    _create_db_if_not_exist()
    with open(DB_PATH, 'a+', newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=";", fieldnames=FIELDNAMES, lineterminator='\n')
        di = {
            "Дата": date.today().strftime("%d/%m/%Y"),
            "Файл": filename,
            "Диагноз": diagnosis,
        }
        writer.writerow(di)


def get_rows(number_rows=15):
    _create_db_if_not_exist()
    with open(DB_PATH, newline='', encoding="utf-8") as csvfile:
        rows = [line.strip().split(';') for line in csvfile.readlines()[1:][-number_rows:]]
        return rows
