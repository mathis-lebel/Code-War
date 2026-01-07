import unittest
import pathlib
import importlib.util


def load_module():
    p = pathlib.Path(__file__).parent / "Largest Greatest Common Divisor.py"
    spec = importlib.util.spec_from_file_location("lgcd", str(p))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.get_k


class TestSampleCodewars(unittest.TestCase):
    def setUp(self):
        self.get_k = load_module()

    def test_codewars_samples(self):
        self.assertEqual(self.get_k(5, 7), 1)
        self.assertEqual(self.get_k(2, 10), 6)
        self.assertEqual(self.get_k(100, 200), 100)
        self.assertEqual(self.get_k(123, 456), 210)


if __name__ == '__main__':
    unittest.main()
