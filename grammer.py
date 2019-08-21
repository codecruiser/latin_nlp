
class Grammer:
    """
    Generates all x-gram representation of text.
    """

    def __init__(self, text=None):
        self.text = text
        self.structured_text = []
        self.skip_grams = []

    def slice_text_to_struct(self):
        """
        Slices full_text into sentences, subsentences and word.

        """
        sentence = []
        subsentence = []
        for word in self.text.slice(' '):
            if word.endswith(','):
                subsentence.append(word[0:-1])
                sentence.append(subsentence.copy())
                #reset subsentence
                subsentence = []
            elif word.endswith('.'):
                subsentence.append(word[0:-1])
                sentence.append(subsentence.copy())
                self.structured_text.append(sentence.copy())
                # reset both
                sentence = []
                subsentence = []
            else:
                subsentence.append(word)

    def generate_skip_gram(self):
        for sentence in self.structured_text:
            for subsentence in sentence:
                for idx, word in enumerate(subsentence):
                    # skip first and last word
                    if idx == 0 or idx+1 == len(subsentence):
                        continue
                    self.skip_grams.append(([word[idx-1], word[idx+1]], word))
