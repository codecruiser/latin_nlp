import pickle

import gensim
import logging


class W2V:

    def __init__(self):
        self.logger = logging.getLogger('W2V')
        self.preprocessed =[]
        self.model = None

    def load(self):
        self.logger.info("reads corpora file... ")
        for line in self._read_file():
            line_preprocessed = gensim.utils.simple_preprocess(line)
            if line_preprocessed:
                self.preprocessed.append(line_preprocessed)

    def save_model(self):
        with open("w2v_model", "wb") as fh:
            pickle.dump(self.model, fh)

    def load_model(self):
        with open("w2v_model", "rb") as fh:
            self.model = pickle.load(fh)

    def train(self):
        """
        Trains gathered word lists with W2V model

        """

        self.logger.info("starts training session... ")
        print("Starts training..")

        try:
            self.load_model()
        except EOFError:
            pass

        if not self.model:
            self.model = gensim.models.Word2Vec(
                self.preprocessed,
                size=150,
                window=10,
                min_count=2,
                workers=10,
                iter=10
            )

            self.save_model()
        print("Ends training..")

    def find_similar(self, word):

        self.logger.info("finds word... ")

        similar = self.model.wv.most_similar(positive=word)
        print(similar)

    def _read_file(self):
        """
        Just reads file and gets data from it.

        :return: yields lines from file
        """
        with open('corpora/latin.txt') as fh:
            for line in fh.read().split('\n'):
                if line:
                    yield line

w2v = W2V()
w2v.load()
w2v.train()
w2v.find_similar('lux')
