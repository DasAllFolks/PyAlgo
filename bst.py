# -*- coding: utf-8 -*-


class BinarySearchTree(object):
  """Implements a basic binary search tree in Python.

  This BST does not do any kind of balancing, and thus can degenerate into a
  linked list in the worst case.
  """

  class _Node(object):
    """Represents a node in the binary search tree."""

    value = None
    left = None
    right = None

  size = 0

  _root = None

  def __init__(self, data=None):
    """Creates a new binary search tree.

    Args:
      data: An optional tuple or list containing data to be inserted IN ORDER
      into the BST.  If not supplied, the BST is created empty.
    """
    for datum in (data or []):
      self.insert(datum)

  @property
  def root(self):
    """Returns the value of the root node.

    If BST is empty, raises a ValueError (i.e., there's no root node to query).
    """
    try:
      return self._root.value
    except AttributeError:
      raise ValueError('Tree is empty; no root node to query.')
