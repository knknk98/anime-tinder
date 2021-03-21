from gensim.models import word2vec
import MeCab
import numpy as np

MECAB_DIC_DIR = "/usr/local/lib/mecab/dic/mecab-ipadic-neologd"


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


if __name__ == "__main__":
    vectorizer = Vectorizer()
    a1 = vectorizer.vectrize("新世紀エヴァンゲリオン")
    a2 = vectorizer.vectrize("機動戦士ガンダム")
    a3 = vectorizer.vectrize("アイドルマスターシンデレラガールズ")
    print(cos_sim(a1, a2))
    print(cos_sim(a1, a3))
    print(cos_sim(a2, a3))
