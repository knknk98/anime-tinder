import argparse
import csv

from gensim.models import word2vec


class Vectorizer:
    def __init__(self):
        self.model = word2vec.Word2Vec.load("vectrized_anime.model")
        self.tagger = MeCab.Tagger("-Owakati" + " -d " + MECAB_DIC_DIR)

    def vectrize(self, text):
        text = self.tagger.parse(text)
        sentences = text.split()
        vec = np.zeros(200)
        for s in sentences:
            try:
                vec += self.model[s]
            except KeyError:
                continue

        return vec


def cos_sim(v1, v2):
    inner = np.dot(v1, v2)
    norms = np.linalg.norm(v1) * np.linalg.norm(v2)
    if norms < 0.01:
        norms = 1

    cos_sim = inner / norms
    return cos_sim


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path to the databese csv")
    args = parser.parse_args()
    with open(args.path) as fp:
        reader = csv.reader(fp)
        for row in reader:
            idx, title, pic_name, description, year, genre, company = row
            print(idx)