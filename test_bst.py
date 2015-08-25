# -*- coding: utf-8 -*-


import unittest

import bst


class TestDelete(unittest.TestCase):
  """Tests deletion of nodes from BST."""

  def test_key_not_found(self):
    root = bst.BinaryNode.build_bst([4, 5, 2, 1, 3])
    new_root, result = root.delete(6)
    self.assertEqual(root, new_root)
    self.assertFalse(result)
    self.assertEqual(new_root.size, 5)

  def test_tree_has_one_node_and_key_is_root(self):
    root = bst.BinaryNode('fred')
    root, result = root.delete('fred')
    self.assertIsNone(root)
    self.assertTrue(result)

  # XXXX: Finish these.


class TestInit(unittest.TestCase):
  """Tests creation of a new binary search tree."""

  def test_new_bst(self):
    """By default, a new binary search tree should consist of just a root."""
    root = bst.BinaryNode('blah')
    self.assertEqual(root.size, 1)


class TestInorder(unittest.TestCase):
  """Tests in-order traversal of binary search tree."""

  def test_empty_tree(self):
    """An empty BST should produce empty list as in-order traversal output."""
    self.assertEqual(None, [])

  def test_single_node(self):
    """A BST with just a root should return a singleton list."""
    self.assertEqual(bst.BinaryNode('fred').inorder, ['fred'])

  def test_multiple_nodes(self):
    """A BST with multiple nodes in any order should return them in order."""
    root = bst.BinaryNode.build_bst([4, 2, 1, 3])
    self.assertEqual(root.inorder, [1, 2, 3, 4])

  def test_multiple_nodes2(self):
    root = bst.BinaryNode.build_bst([4, 5, 2, 1, 3])
    self.assertEqual(root.inorder, [1, 2, 3, 4, 5])


class TestInsert(unittest.TestCase):
  """Tests insertion into a binary search tree."""

  def test_insert_into_empty_tree(self):
    """Anything inserted into an empty BST should become root."""
    tree = bst.BinarySearchTree()
    self.assertTrue(tree.insert(42))
    self.assertEqual(tree.size, 1)
    self.assertEqual(tree.root, 42)

  def test_insert_duplicate_root(self):
    """A tree will not permit duplicates to be inserted."""
    tree = bst.BinarySearchTree([1])
    self.assertFalse(tree.insert(1))
    self.assertEqual(tree.size, 1)
    self.assertEqual(tree.root, 1)

  def test_insert_duplicate_leaf(self):
    """Leaves can't be duplicated either."""
    tree = bst.BinarySearchTree([1, 2])
    self.assertFalse(tree.insert(2))
    self.assertEqual(tree.size, 2)
    self.assertEqual(tree.root, 1)

  def test_insert_left(self):
    tree = bst.BinarySearchTree([2])
    self.assertTrue(tree.insert(1))
    self.assertEqual(tree.size, 2)
    self.assertEqual(tree.root, 2)
    self.assertEqual(tree.inorder, [1, 2])

  def test_insert_right(self):
    tree = bst.BinarySearchTree([2])
    self.assertTrue(tree.insert(3))
    self.assertEqual(tree.size, 2)
    self.assertEqual(tree.root, 2)
    self.assertEqual(tree.inorder, [2, 3])


class TestPreorder(unittest.TestCase):
  """Tests preorder traversal of binary search tree."""

  def test_empty_tree(self):
    """An empty BST should produce empty list as preorder traversal output."""
    self.assertEqual(bst.BinarySearchTree().preorder, [])

  def test_single_node(self):
    """A BST with just a root should return a singleton list."""
    self.assertEqual(bst.BinarySearchTree(['fred']).preorder, ['fred'])

  def test_multiple_nodes(self):
    tree = bst.BinarySearchTree([4, 5, 2, 1, 3])
    self.assertEqual(tree.preorder, [4, 2, 1, 3, 5])


class TestPostorder(unittest.TestCase):
  """Tests postorder traversal of binary search tree."""

  def test_empty_tree(self):
    """An empty BST should produce empty list as postorder traversal output."""
    self.assertEqual(bst.BinarySearchTree().preorder, [])

  def test_single_node(self):
    """A BST with just a root should return a singleton list."""
    self.assertEqual(bst.BinarySearchTree(['fred']).postorder, ['fred'])

  def test_multiple_nodes(self):
    tree = bst.BinarySearchTree([4, 5, 2, 1, 3])
    self.assertEqual(tree.postorder, [1, 3, 2, 5, 4])


class TestSearch(unittest.TestCase):
  """Tests ability to search for a given value within the BST."""

  def test_empty_tree(self):
    tree = bst.BinarySearchTree()
    self.assertFalse(tree.search(1))

  def test_nonempty_tree_key_not_found(self):
    tree = bst.BinarySearchTree([4, 5, 2, 1, 3])
    self.assertFalse(tree.search(6))

  def test_tree_has_one_node_and_key_is_root(self):
    tree = bst.BinarySearchTree(['fred'])
    self.assertTrue(tree.search('fred'))

  def test_tree_has_multiple_nodes_and_key_is_leaf(self):
    tree = bst.BinarySearchTree([4, 5, 2, 1, 3])
    self.assertTrue(tree.search(5))

  def test_tree_has_multiple_nodes_and_key_is_neither_root_nor_leaf(self):
    tree = bst.BinarySearchTree([4, 5, 2, 1, 3])
    self.assertTrue(tree.search(2))
