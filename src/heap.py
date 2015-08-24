# -*- coding: utf-8 -*-


class Heap(object):
  """Implements a heap data structure in Python.

  The underlying data structure used to hold the data is an array.
  """

  __heap = []

  def __init__(self, initial=[]):
    """Creates a new heap.

    Args:
      initial: (Optional): A continguous array containing the data with which to
        initialize the new heap.
    """
    self.__heap = []
