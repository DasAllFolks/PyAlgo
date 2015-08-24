# -*- coding: utf-8 -*-


import unittest

import heap


class TestHeap(unittest.TestCase):
  """Tests the heap data structure."""

  def test_created_empty(self):
    """By default, a new heap should be created empty."""
    h = heap.Heap()
    self.assertEqual(h.size, 0)
    with self.assertRaises(ValueError):
      h.pop()
