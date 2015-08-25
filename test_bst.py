# -*- coding: utf-8 -*-


import unittest

import bst


class TestInit(unittest.TestCase):
  """Tests creation of a new binary search tree."""

  def test_empty_by_default(self):
    """By default, a new binary search tree should be created empty."""
    tree = bst.BinarySearchTree()
    with self.assertRaises(ValueError):
      tree.root
    self.assertEqual(tree.size, 0)
    self.assertEqual(tree.preorder, [])
    self.assertEqual(tree.inorder, [])
    self.assertEqual(tree.postorder, [])


class TestInorder(unittest.TestCase):
  """Tests in-order traversal of binary search tree."""

  def test_empty_tree(self):
    """An empty BST should produce empty list as in-order traversal output."""
    self.assertEqual(bst.BinarySearchTree().inorder, [])

  def test_single_node(self):
    """A BST with just a root should return a singleton list."""
    self.assertEqual(bst.BinarySearchTree(['fred']).inorder, ['fred'])

  def test_multiple_nodes(self):
    """A BST with multiple nodes in any order should return them in order."""
    tree = bst.BinarySearchTree([4, 2, 1, 3])
    self.assertEqual(tree.inorder, [1, 2, 3, 4])


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
