import argparse
import json
import os

from gensim.models import word2vec
import MeCab
from tqdm import tqdm
from logzero import logger


MECAB_DIC_DIR = "/usr/local/lib/mecab/dic/mecab-ipadic-neologd"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path to the anime article json")
    args = parser.parse_args()

    if not os.path.exists("all_article.txt"):
        create_merged_article(args)

    if not os.path.exists("vectrized_anime.model"):
        create_model(args)


def create_merged_article(args):
    logger.info("Merging the all article...")
    tagger = MeCab.Tagger("-Owakati" + " -d " + MECAB_DIC_DIR)
    all_article = ""
    with open(args.path) as fp:
        for line in tqdm(fp):
            animeinfo = json.loads(line)
            article = animeinfo["article"]
            article = article.replace("\n", "")
            article = tagger.parse(article)

            all_article += article

    with open("all_article.txt", "w") as fp:
        fp.write(all_article)

    logger.info("Finished! 'all_article.txt' created.")


def create_model(args):
    sentences = word2vec.LineSentence("all_article.txt")
    logger.info("creating the model...")
    model = word2vec.Word2Vec(sentences, sg=1, size=200, min_count=1, window=3)
    model.save("vectrized_anime.model")


if __name__ == "__main__":
    main()
