git clone https://github.com/attardi/wikiextractor.git
curl https://dumps.wikimedia.org/jawiki/latest/jawiki-latest-pages-articles.xml.bz2 -o jawiki-latest-pages-articles.xml.bz2
python wikiextractor/WikiExtractor.py jawiki-latest-pages-articles.xml.bz2 -b 5G
python extract_anime_article.py animeinfo.json > anime_article.jsonl