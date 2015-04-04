from Node import Node


class Tree:
    def __init__(self):
        self.root_node = Node.factory(None)

    def insert(self, new_node):
        self.__insert_node(new_node, self.root_node)

    def __insert_node(self, new_node, root_node):
        if root_node.is_empty():
            root_node.assign(new_node)
        elif new_node < root_node:
            self.__insert_node(new_node, root_node.left)
        elif new_node >= root_node:
            self.__insert_node(new_node, root_node.right)

    def print_tree(self, node):
        if node.is_empty():
            return
        self.print_tree(node.left)
        print(node)
        self.print_tree(node.right)

    def search(self, node):
        return self.__search_node(node, self.root_node)

    def __search_node(self, node, root_node):
        if node.is_empty() or root_node.is_empty():
            result = False
        elif node == root_node:
            result = node == root_node
        elif node < root_node:
            result = self.__search_node(node, root_node.left)
        else:
            result = self.__search_node(node, root_node.right)
        return result

