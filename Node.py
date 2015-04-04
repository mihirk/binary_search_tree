class Node:
    def __init__(self, value=None):
        self.value = value

    @classmethod
    def factory(cls, value=None):
        node = cls(value)
        node.left = cls()
        node.right = cls()
        return node

    def __cmp__(self, other):
        return self.value.__cmp__(other.value)

    def __str__(self):
        return str(self.value)

    def is_empty(self):
        return self.value is None

    def assign(self, node):
        self.value = node.value
        self.left = node.left
        self.right = node.right