from Node import Node


class Tree:
    def __init__(self):
        self.root_node = Node.factory()

    def insert(self, new_node):
        if new_node is not None and not new_node.is_empty():
            self.__insert_node(new_node, self.root_node)

    def __insert_node(self, new_node, root_node):
        if root_node.is_empty():
            root_node.assign(new_node)
        elif new_node < root_node:
            self.__insert_node(new_node, root_node.left)
        elif new_node > root_node:
            self.__insert_node(new_node, root_node.right)
        
    def inorder(self):
        return self.__print_tree(self.root_node)

    def __print_tree(self, node):
        if node.is_empty():
            return
        self.__print_tree(node.left)
        print(node)
        self.__print_tree(node.right)

    def search(self, node):
        return self.__search_node(node, self.root_node)

    def __search_node(self, node, root_node):
        if node.is_empty() or root_node.is_empty():
            result = False
        elif node == root_node:
            result = node == root_node
        elif node < root_node:
            result = self.__search_node(node, root_node.left)
        elif node > root_node:
            result = self.__search_node(node, root_node.right)
        return result

    def delete(self, node):
        self.__delete_node(node, self.root_node)

    def __delete_node(self, node, root_node):
        if node == root_node:
            left_subtree = root_node.left
            right_subtree = root_node.right
            root_node.assign(Node.factory())
            self.insert(left_subtree)
            self.insert(right_subtree)
        elif node < root_node:
            self.__delete_node(node, root_node.left)
        elif node > root_node:
            self.__delete_node(node, root_node.right)

    def size(self):
        return self.__size(self.root_node)

    def __size(self, root_node):
        if root_node.is_empty():
            return 0
        else:
            return self.__size(root_node.left) + self.__size(root_node.right) + 1