import unittest
import pathlib
import importlib.util


def load_minimum():
    p = pathlib.Path(__file__).parent / "MinimumValue.py"
    spec = importlib.util.spec_from_file_location("minmod", str(p))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.minimum_value


class TestMinimumValue(unittest.TestCase):
    def setUp(self):
        self.minimum_value = load_minimum()

    def test_single_var(self):
        self.assertAlmostEqual(self.minimum_value('x=1'), 1.0)

    def test_coefficient(self):
        self.assertAlmostEqual(self.minimum_value('2x=4'), 4.0)

    def test_two_vars(self):
        self.assertAlmostEqual(self.minimum_value('x+y=3'), 4.5)

    def test_negative_coeff(self):
        self.assertAlmostEqual(self.minimum_value('-x+2y=5'), 5.0)


if __name__ == '__main__':
    unittest.main()
