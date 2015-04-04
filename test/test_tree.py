from unittest import TestCase
from Node import Node
from Tree import Tree


class TestTree(TestCase):
    def test_tree_initialization(self):
        tree = Tree()
        self.assertIsNotNone(tree.root_node)
        self.assertIsNone(tree.root_node.value)
        self.assertIsNone(tree.root_node.left.value)
        self.assertIsNone(tree.root_node.right.value)

    def test_tree_insertion_root_node(self):
        tree = Tree()
        self.assertIsNotNone(tree.root_node)
        self.assertIsNone(tree.root_node.value)
        self.assertIsNone(tree.root_node.left.value)
        self.assertIsNone(tree.root_node.right.value)
        tree.insert(Node.factory(12))
        self.assertIsNotNone(tree.root_node)
        self.assertIsNotNone(tree.root_node.value)
        self.assertEqual(12, tree.root_node.value)
        self.assertIsNone(tree.root_node.left.value)
        self.assertIsNone(tree.root_node.right.value)

    def test_tree_insertion_right_node(self):
        tree = Tree()
        tree.insert(Node.factory(12))
        tree.insert(Node.factory(15))
        self.assertIsNotNone(tree.root_node)
        self.assertIsNotNone(tree.root_node.value)
        self.assertEqual(12, tree.root_node.value)
        self.assertIsNone(tree.root_node.left.value)
        self.assertIsNotNone(tree.root_node.right.value)
        self.assertEqual(15, tree.root_node.right.value)

    def test_tree_insertion_left_node(self):
        tree = Tree()
        tree.insert(Node.factory(12))
        tree.insert(Node.factory(10))
        self.assertIsNotNone(tree.root_node)
        self.assertIsNotNone(tree.root_node.value)
        self.assertEqual(12, tree.root_node.value)
        self.assertIsNotNone(tree.root_node.left.value)
        self.assertIsNone(tree.root_node.right.value)
        self.assertEqual(10, tree.root_node.left.value)

    def test_tree_insertion_equal_node(self):
        tree = Tree()
        tree.insert(Node.factory(12))
        tree.insert(Node.factory(12))
        self.assertIsNotNone(tree.root_node)
        self.assertIsNotNone(tree.root_node.value)
        self.assertEqual(12, tree.root_node.value)
        self.assertIsNone(tree.root_node.left.value)
        self.assertIsNotNone(tree.root_node.right.value)
        self.assertEqual(12, tree.root_node.right.value)

    def test_tree_multi_level_insertion(self):
        tree = Tree()
        tree.insert(Node.factory(12))
        tree.insert(Node.factory(12))
        tree.insert(Node.factory(10))
        tree.insert(Node.factory(11))
        tree.insert(Node.factory(1))
        tree.insert(Node.factory(100))
        self.assertEqual(12, tree.root_node.value)
        self.assertEqual(12, tree.root_node.right.value)
        self.assertEqual(100, tree.root_node.right.right.value)
        self.assertEqual(10, tree.root_node.left.value)
        self.assertEqual(11, tree.root_node.left.right.value)
        self.assertEqual(1, tree.root_node.left.left.value)