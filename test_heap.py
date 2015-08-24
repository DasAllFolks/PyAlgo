# -*- coding: utf-8 -*-


import unittest

import heap


class TestInit(unittest.TestCase):
  """Tests creation of a new heap."""

  def test_created_empty(self):
    """By default, a new heap should be created empty."""
    h = heap.Heap()
    self.assertEqual(h.size, 0)


class TestPoll(unittest.TestCase):
  """Tests polling of heap's root element.

  I.e., where by "polling," we mean examining the value of the heap's root
  element WITHOUT removing it or otherwise altering the heap's state in any way.
  """

  def test_empty(self):
    """Polling an empty heap should raise a ValueError."""
    with self.assertRaises(ValueError):
      heap.Heap().poll()

  def test_one_node(self):
    """Polling a heap with one node should return that node's value."""
    self.assertEqual(heap.Heap([1]).poll(), 1)

  def test_multiple_nodes(self):
    """Polling a heap with many nodes should return the root node's value."""
    self.assertEqual(heap.Heap([6, None, 'fred']), 6)


class TestPop(unittest.TestCase):
  """Tests our ability to remove the top element from the heap."""
  pass


class TestPush(unittest.TestCase):
  """Tests our ability to push a new element onto the heap."""
  pass
