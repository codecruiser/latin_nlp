import re


def word_cleaning(words):
    """
    Preprocessing - cleans words of any "dirt".

    :param words: list of words
    :return: cleaned list of words.
    """
    replacements = {
        "ā": "a", "ē": "e", "ī": "i", "ō": "o", "ū": "u",
        "Ā": "a", "Ē": "e", "Ī": "i", "Ō": "o", "Ū": "u",
        "ă": "a", "ŭ": "u"
    }

    words_cleaned = []
    for word in words:
        for char_in, char_out in replacements:
            word = word.replace(char_in, char_out)
            cleaned = re.sub(r'[^a-z]', '', word.lower())
            if cleaned:
                words_cleaned.append(cleaned)

    return words_cleaned


def extract_stop_words(filename):
    """
    Stop words extraction from corpora text.

    :param filename: corpora filename
    :return:
    """

    with open(filename) as fh:
        content = fh.read()
        cleaned = word_cleaning(content.split(' '))

        frequency = {}
        for word in cleaned:
            frequency[word] += 1 if word in frequency else 1

        frequency = sorted(frequency.items(), key=lambda kv: (kv[1], kv[0]))

    return frequency
