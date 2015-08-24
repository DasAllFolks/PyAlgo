# -*- coding: utf-8 -*-


class Heap(object):
  """Implements a heap data structure in Python.

  The underlying data structure used to hold the data is a list.
  """

  _heap = []

  def __init__(self, initial=None):
    """Creates a new heap.

    Args:
      initial: (Optional): A continguous list containing the data with which to
        initialize the new heap.
    """
    if isinstance(initial, list) or isinstance(initial, tuple):
      self._heap = initial
    elif initial is not None:
      raise TypeError(
        'Illegal type submitted for heap data; use a list or tuple instead.')

  def __unicode__(self):
    if not self._heap:
      return 'Empty'
    return 'Root: %s' % self.__heap[0]
