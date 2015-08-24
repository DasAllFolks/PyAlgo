# -*- coding: utf-8 -*-


class Heap(object):
  """Implements a heap data structure in Python.

  The underlying data structure used to hold the data is a list.
  """

  __heap = []

  def __init__(self, initial=None):
    """Creates a new heap.

    Args:
      initial: (Optional): A continguous list containing the data with which to
        initialize the new heap.
    """
    if isinstance(initial, list) or isinstance(initial, tuple):
      self.__heap = initial
    elif initial is not None:
      raise TypeError(
        'Illegal type submitted for heap data; use a list or tuple instead.')

  def __unicode__(self):
    if not self.__heap:
      return 'Empty'
    return 'Root: %s' % self.__heap[0]

  def poll(self):
    """Gets the value of the heap's root node WITHOUT removing it.

    Raises:
      ValueError:  If the heap is empty.
    """
    try:
      return self.__heap[0]
    except KeyError:
      raise ValueError('Heap is empty')

  @property
  def size(self):
    """Returns a nonnegative integer giving number of elements in the heap."""
    return len(self.__heap)
