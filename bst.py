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

  _root = None
  _size = 0

  def __init__(self, data=None):
    """Creates a new binary search tree.

    Args:
      data: An optional tuple or list containing data to be inserted IN ORDER
      into the BST.  If not supplied, the BST is created empty.
    """
    for datum in (data or []):
      self.insert(datum)

  @property
  def inorder(self):
    """Returns values of all nodes in order, as a list.

    For an empty BST, this returns an empty list.
    """
    return self.__inorder(self._root)

  def insert(self, value):
    """Inserts a new value into the BST (without rebalancing the tree).

    Returns True if the value was successfully inserted, False otherwise (e.g.,
    probably because the value duplicated an existing value in the BST).
    """
    self._root, result = self.__insert(value, self._root)
    self._size += int(result)
    return result

  @property
  def postorder(self):
    """Returns list of values generated by postorder traversal of tree.

    For an empty BST, this returns an empty list.
    """
    return self.__postorder(self._root)

  @property
  def preorder(self):
    """Returns list of values generated by preorder traversal of tree.

    For an empty BST, this returns an empty list.
    """
    return self.__preorder(self._root)

  @property
  def root(self):
    """Returns the value of the root node.

    If BST is empty, raises a ValueError (i.e., there's no root node to query).
    """
    try:
      return self._root.value
    except AttributeError:
      raise ValueError('Tree is empty; no root node to query.')

  def search(self, value):
    """Returns True if value is found in BST, False otherwise."""
    pass

  @property
  def size(self):
    """Returns the number of elements in the BST as an int."""
    return self._size

  def __inorder(self, root):
    """Returns values of all nodes in a subtree in order, as a list.

    For an empty subtree (defined by a root of None), this returns an empty
    list.
    """
    if not root:
      return []
    return self.__inorder(root.left) + [root.value] + self.__inorder(root.right)

  def __insert(self, value, root):
    """Attempts to insert the given value into the subtree with the given root.

    Returns True if the value was successfully inserted, False otherwise (e.g.,
    probably because the value duplicated an existing value in the BST).
    """
    if not root:
      return self._Node(value), True

    if value < root.value:
      root.left, result = self.__insert(value, root.left)
      return root, result

    if value > root.value:
      root.right, result = self.__insert(value, root.right)
      return root, result

    return root, False

  def __postorder(self, root):
    """Returns list of values generated by postorder traversal of a subtree.

    For an empty subtree, this returns an empty list.
    """
    if not root:
      return []
    return (
      self.__postorder(root.left) + self.__postorder(root.right) + [root.value])

  def __preorder(self, root):
    """Returns list of values generated by preorder traversal of a subtree.

    For an empty subtree, this returns an empty list.
    """
    if not root:
      return []
    return (
      [root.value] + self.__preorder(root.left) + self.__preorder(root.right))
