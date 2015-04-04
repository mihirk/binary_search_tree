class WordWrapper:
    def __init__(self, word):
        word = word.replace(',', '')
        word = word.replace('.', '')
        self.word = word

    def __cmp__(self, other):
        return cmp(self.word, other.word)

    def __str__(self):
        return str(self.word)

