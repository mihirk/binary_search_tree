from Tree import Tree
from Node import Node
from WordWrapper import WordWrapper


class TextFile:
    def __init__(self, file_path):
        self.tree = Tree()
        with open(file_path) as f:
            for line in f:
                for word in line.split():
                    self.tree.insert(Node.factory(WordWrapper(word)))

    def word_count(self):
        return self.tree.size()
