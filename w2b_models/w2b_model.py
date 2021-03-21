from gensim.models import Word2Vec
import MeCab
import numpy as np

MECAB_DIC_DIR = "/usr/local/lib/mecab/dic/mecab-ipadic-neologd"


class Vectorizer:
    def __init__(self):
        self.model = Word2Vec.load("vectrized_anime.model")
        self.tagger = MeCab.Tagger("-Owakati" + " -d " + MECAB_DIC_DIR)

    def vectrize(self, text):
        text = self.tagger.parse(text)
        sentences = text.split()
        vec = np.zeros(200)
        for s in sentences:
            try:
                vec = vec + self.model.wv[s]
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


if __name__ == "__main__":
    # demo of the model
    vectorizer = Vectorizer()
    while True:
        print("Input the two anime title")
        print(">>>", end="")
        a = input().split()
        v1 = vectorizer.vectrize(a[0])
        v2 = vectorizer.vectrize(a[1])
        sim = cos_sim(v1, v2)
        print(f"Simirality between them\n= {sim}\n")


