from __future__ import print_function
from Node import Node
from Tree import Tree

node1 = Node.factory(1)
node2 = Node.factory(2)
node3 = Node.factory(3)
node6 = Node.factory(10)
node4 = Node.factory(11)
node5 = Node.factory(12)
tree = Tree()
tree.insert(node6)
tree.insert(node1)
tree.insert(node2)
tree.insert(node3)
tree.insert(node4)
tree.insert(node5)
tree.print_tree(tree.root_node)
# print(tree.search(Node.factory(3)))
tree.delete(Node.factory(3))
print("\n")
# print(tree.search(Node.factory(3)))
tree.print_tree(tree.root_node)
