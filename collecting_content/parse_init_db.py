import csv
import re
from urllib.parse import urlencode

import requests
from bs4 import Beautiful

def create_csv_from_sql():
    with open("init_db.txt") as fp:
        text = fp.read()

    rows = text.split("),(")

    rows[0] = rows[0][1:]
    rows[-1] = rows[-1][:-1]
    for r in rows:
        print(r)

def arrange_csv():
    with open("init_db.csv") as fp:
        reader = csv.reader(fp)
        with open("new_init_db.csv", "w") as fw:
            writer = csv.writer(fw)

            for row in reader:

                title = row[1]
                description = row[3]
                if description == "description":
                    url = "https://ja.wikipedia.org/wiki/" + urlencode(title)
                    


if __name__ == "__main__":
    arrange_csv()