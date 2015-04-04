from unittest import TestCase
from Node import Node


class NodeTest(TestCase):
    def test_node_factory(self):
        node = Node.factory(12)
        self.assertEqual(12, node.value)
        self.assertIsNone(node.left.value)
        self.assertIsNone(node.right.value)

    def test_node_factory_none_case(self):
        self.assertIsNone(Node.factory(None).value)
        self.assertIsNone(Node.factory(None).left.value)
        self.assertIsNone(Node.factory(None).right.value)

    def test_node_comparison_based_on_value(self):
        self.assertTrue(Node(1) < Node(2))
        self.assertFalse(Node(1) > Node(2))
        self.assertTrue(Node(1) == Node(1))
        self.assertFalse(Node(1) > Node(1))
        self.assertFalse(Node(1) < Node(1))

    def test_node_string_output_of_value(self):
        self.assertEqual("1", str(Node(1)))
        self.assertEqual("None", str(Node(None)))
        self.assertEqual("55", str(Node(55)))

    def test_node_empty(self):
        self.assertFalse(Node(1).is_empty())
        self.assertTrue(Node().is_empty())

    def test_node_assignment(self):
        node1 = Node.factory(25)
        node2 = Node.factory(None)
        self.assertIsNone(node2.value)
        self.assertIsNone(node2.left.value)
        self.assertIsNone(node2.right.value)
        node2.assign(node1)
        self.assertEqual(25, node2.value)
        self.assertIsNone(node2.left.value)
        self.assertIsNone(node2.right.value)
        node1.left = Node.factory(15)
        node1.right = Node.factory(35)
        node2.assign(node1)
        self.assertEqual(25, node2.value)
        self.assertEqual(15, node2.left.value)
        self.assertEqual(35, node2.right.value)