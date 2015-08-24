import unittest


class TestTest(unittest.TestCase):
  def test_succeeds(self):
    self.assertTrue(True)

  def test_fails(self):
    self.assertFalse(True)
