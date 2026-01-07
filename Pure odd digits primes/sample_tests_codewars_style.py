import unittest
import pathlib
import importlib.util


def load_module():
    p = pathlib.Path(__file__).parent / "Pure odd digits primes.py"
    spec = importlib.util.spec_from_file_location("podp", str(p))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.odd_dig_primes


class TestSampleCodewars(unittest.TestCase):
    def setUp(self):
        self.odd_dig_primes = load_module()

    def test_codewars_samples(self):
        self.assertEqual(self.odd_dig_primes(20), [7, 19, 31])
        self.assertEqual(self.odd_dig_primes(40), [9, 37, 53])


if __name__ == '__main__':
    unittest.main()
