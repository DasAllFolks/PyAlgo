# -*- coding: utf-8 -*-


import unittest

import heap


class TestInit(unittest.TestCase):
  """Tests creation of a new heap."""

  def test_created_empty(self):
    """By default, a new heap should be created empty."""
    h = heap.Heap()
    self.assertEqual(h.size, 0)
    with self.assertRaises(ValueError):
      h.poll()
    with self.assertRaises(ValueError):
      h.pop()


class TestPoll(unittest.TestCase):
  """Tests polling of heap's root element.

  I.e., where by "polling," we mean examining the value of the heap's root
  element WITHOUT removing it or otherwise altering the heap's state in any way.
  """
  pass


class TestPop(unittest.TestCase):
