import unittest
import pathlib
import importlib.util


def load_minimum():
    p = pathlib.Path(__file__).parent / "MinimumValue.py"
    spec = importlib.util.spec_from_file_location("minmod", str(p))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.minimum_value


class ColorResult(unittest.TextTestResult):
    COLORS = {
        'pass': '\033[32m',
        'fail': '\033[31m',
        'error': '\033[31m',
        'skip': '\033[33m',
        'reset': '\033[0m'
    }

    def getDescription(self, test):
        doc = test.shortDescription()
        return doc if doc else str(test)

    def addSuccess(self, test):
        super().addSuccess(test)
        self.stream.writeln(f"{self.COLORS['pass']}[PASS]{self.COLORS['reset']} {self.getDescription(test)}")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.stream.writeln(f"{self.COLORS['fail']}[FAIL]{self.COLORS['reset']} {self.getDescription(test)}")

    def addError(self, test, err):
        super().addError(test, err)
        self.stream.writeln(f"{self.COLORS['error']}[ERROR]{self.COLORS['reset']} {self.getDescription(test)}")

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        self.stream.writeln(f"{self.COLORS['skip']}[SKIP]{self.COLORS['reset']} {self.getDescription(test)} - {reason}")


class ColorTextTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        return ColorResult(self.stream, self.descriptions, self.verbosity)


class TestMinimumValue(unittest.TestCase):
    def setUp(self):
        self.minimum_value = load_minimum()

    def test_single_var(self):
        """minimum_value('x=1') -> 1.0"""
        self.assertAlmostEqual(self.minimum_value('x=1'), 1.0)

    def test_coefficient(self):
        """minimum_value('2x=4') -> 4.0"""
        self.assertAlmostEqual(self.minimum_value('2x=4'), 4.0)

    def test_two_vars(self):
        """minimum_value('x+y=3') -> 4.5"""
        self.assertAlmostEqual(self.minimum_value('x+y=3'), 4.5)

    def test_negative_coeff(self):
        """minimum_value('-x+2y=5') -> 5.0"""
        self.assertAlmostEqual(self.minimum_value('-x+2y=5'), 5.0)


if __name__ == '__main__':
    unittest.main(testRunner=ColorTextTestRunner(verbosity=0))
