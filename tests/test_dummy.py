import unittest


class Dummy(unittest.TestCase):

    def test_dummy(self):
        self.assertEqual(42, 7*6)


if __name__ == "__main__":
    # run all tests
    unittest.main()  # pragma: no cover
