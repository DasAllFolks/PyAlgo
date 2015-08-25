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


class TestInsert(unittest.TestCase):
  """Tests insertion into a binary search tree."""

  def test_insert_into_empty_tree(self):
    """Anything inserted into an empty BST should become root."""
    tree = bst.BinarySearchTree()
    tree.insert(42)
    self.assertEqual(tree.size, 1)
    self.assertEqual(tree.root, 42)
