from Node import Node


class Tree:
    def __init__(self):
        self.root_node = Node.factory(None)

    def insert(self, new_node):
        self.insert_node(new_node, self.root_node)

    def insert_node(self, new_node, root_node):
        if root_node.is_empty():
            root_node.assign(new_node)
        elif new_node < root_node:
            self.insert_node(new_node, root_node.left)
        elif new_node >= root_node:
            self.insert_node(new_node, root_node.right)

    def print_tree(self, node):
        if node.is_empty():
            return
        self.print_tree(node.left)
        print(node)
        self.print_tree(node.right)