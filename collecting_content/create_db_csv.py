import csv
import json

import requests
from bs4 import BeautifulSoup
from logzero import logger

OLDEST_YEAR_TO_FETCH = 2016


def main():
    with open("animeinfo.json") as fp:
        animeinfo = json.load(fp)

    with open("anime_db.csv", "w", errors="ignore") as fp:
        writer = csv.writer(fp)
        writer.writerow(
            ["id", "title", "figure_path", "description", "year", "genre", "company"]
        )

        db_id = 1
        current_year = OLDEST_YEAR_TO_FETCH
        count_per_year = 0
        for idx, info in animeinfo.items():
            title = info["title"]
            year = info["year"]
            if int(year) < OLDEST_YEAR_TO_FETCH:
                continue

            if current_year != int(year):
                count_per_year = 0

            if count_per_year > 50:
                continue

            url = info["url"]
            html = requests.get(url).text
            soup = BeautifulSoup(html, "html.parser")

            logger.info(f"{title} collecting")
            description = get_description(soup)
            genre = get_genre(soup)
            company = get_company(soup)
            title = title.replace(",", "")
            writer.writerow(
                [
                    db_id,
                    title,
                    "unknown.png",
                    description,
                    year,
                    genre,
                    company,
                ],
            )
            db_id += 1
            count_per_year += 1

            if db_id > 200:
                break


def get_genre(soup):
    try:
        link_area = soup.select_one(
            "#mw-content-text > div.mw-parser-output > table.infobox.bordered"
        )
        rows = link_area.find_all("tr")

        for row in rows:
            elements = row.text.split()
            if "ジャンル" in elements:
                genre = " ".join(elements[1:])
                genre.replace(",", "")
                if genre == "":
                    genre = "アニメ"
                return genre

    except:
        return "アニメ"


def get_description(soup):
    try:
        link_area = soup.select_one("#mw-content-text > div.mw-parser-output")
        sentences = link_area.find_all("p")
        text = ""
        for p in e sentences:
            text += p.text.strip()

        text = text.replace(",", "")
        text = text.replace("\n", "")
        return text

    except:
        return "unknown"


def get_company(soup):
    try:
        link_area = soup.select_one(
            "#mw-content-text > div.mw-parser-output > table.infobox.bordered"
        )
        rows = link_area.find_all("tr")
        for row in rows:
            elements = row.text.split()
            if "アニメーション制作" in elements:
                company = " ".join(elements[1:])
                company = company.replace(",", "")
                if company == "":
                    company = "unknown"

                return company

    except:
        return "unknown"


if __name__ == "__main__":
    main()