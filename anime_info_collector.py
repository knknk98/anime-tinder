import dataclasses
import json
from urllib.parse import urlencode

from bs4 import BeautifulSoup
from logzero import logger
import requests


@dataclasses.dataclass
class AnimeInfo:
    """Class for keeping Anime information"""

    pageid: int
    title: str
    genre: str


class InfoCollector:
    def _create_mediawiki_query_form_title(self, title=str) -> str:
        url_base = "https://ja.wikipedia.org/w/api.php"
        query = urlencode(
            {
                "format": "json",
                "action": "query",
                "prop": "revisions",  # 本来記事のリビジョンを取得
                "titles": title,  #
                "rvprop": "content",  # 本文を取得
                "rvparse": "",  # 本文をHTMLで取得
            }
        )
        url = f"{url_base}?{query}"
        return url

    def extract_animeinfo_from_html(self, html: str) -> AnimeInfo:
        soup = BeautifulSoup(html, "html.parser")
        info_table = soup.select(
            "#mw-content-text > div.mw-parser-output > table.infobox.bordered"
        )
        print(info_table)

    def from_mediawiki(self, title: str) -> AnimeInfo:
        """
        Crawling data via [MediaWiki API](https://www.mediawiki.org/wiki/API:Main_page/ja)
        TODO 存在しない記事を引いた際の挙動をスマートにしたい。たとえば類似文字列検索で関連記事を取得してくるとか
        Parameters
        ----------
        title : str
            Title of the content

        Returns
        -------
        AnimeInfo
            [description]
        """
        logger.info(f"[START] Collecting '{title}' from media wiki api")
        query_url = self._create_mediawiki_query_form_title(title)
        r = requests.get(query_url)
        logger.info(f"[FINISH] Collecting '{title}' from media wiki api")

        if r.text:
            content = json.loads(r.text)
            pages = content["query"]["pages"]
            for key, val in pages.items():
                pageid = val["pageid"]
                html = val["revisions"][0]["*"]
                self.extract_animeinfo_from_html(html)


def main():
    InfoCollector().from_mediawiki("ソードアート・オンライン")


if __name__ == "__main__":
    main()
