# -*- coding: utf-8 -*-


import unittest

import bst


class TestInit(unittest.TestCase):
  """Tests creation of a new binary search tree."""

  def test_empty_by_default(self):
    """By default, a new binary search tree should be created empty."""
    tree = bst.BinarySearchTree()
    self.assertEqual(tree.size, 0)
    self.assertEqual(tree.preorder, [])
    self.assertEqual(tree.inorder, [])
    self.assertEqual(tree.postorder, [])
