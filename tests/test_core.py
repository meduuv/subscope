import unittest

from subscope.core import normalize, resolve


class CoreTests(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual(normalize(" Example.COM. "), "example.com")

    def test_invalid(self):
        with self.assertRaises(ValueError):
            normalize("example .com")

    def test_resolve_localhost(self):
        result = resolve("localhost")
        self.assertTrue(result.addresses)


if __name__ == "__main__":
    unittest.main()
