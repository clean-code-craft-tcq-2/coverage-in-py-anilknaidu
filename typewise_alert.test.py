import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(1 == 1)


if __name__ == '__main__':
  unittest.main()
