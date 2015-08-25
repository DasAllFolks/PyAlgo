# -*- coding: utf-8 -*-


class BinarySearchTree(object):
  """Implements a basic binary search tree in Python.

  This BST does not do any kind of balancing, and thus can degenerate into a
  linked list in the worst case.

  This BST also does NOT permit duplicates.
  """

  class _Node(object):
    """Represents a node in the binary search tree."""

    left = None
    right = None

    def __init__(self, value):
      self.value = value

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

  def insert(self, value):
    """Inserts a new value into the BST (without rebalancing the tree).

    Returns True if the value was successfully inserted, False otherwise (e.g.,
    probably because the value duplicated an existing value in the BST).
    """
    if not self._root:
      self._root = _Node(value)
      return True
    return self.__insert(value, self._root)

  @property
  def root(self):
    """Returns the value of the root node.

    If BST is empty, raises a ValueError (i.e., there's no root node to query).
    """
    try:
      return self._root.value
    except AttributeError:
      raise ValueError('Tree is empty; no root node to query.')

  def __insert(self, value, root):
    """Attempts to insert the given value into the subtree with the given root.

    Returns True if the value was successfully inserted, False otherwise (e.g.,
    probably because the value duplicated an existing value in the BST).
    """
    if not root:
      pass
