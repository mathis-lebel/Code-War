import unittest
import pathlib
import importlib.util
import sys


def load_module():
    p = pathlib.Path(__file__).parent / "Pure odd digits primes.py"
    spec = importlib.util.spec_from_file_location("podp", str(p))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.odd_dig_primes


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


class TestSampleCodewars(unittest.TestCase):
    def setUp(self):
        self.odd_dig_primes = load_module()

    def test_case_20(self):
        """odd_dig_primes(20) -> [7, 19, 31]"""
        self.assertEqual(self.odd_dig_primes(20), [7, 19, 31])

    def test_case_40(self):
        """odd_dig_primes(40) -> [9, 37, 53]"""
        self.assertEqual(self.odd_dig_primes(40), [9, 37, 53])


if __name__ == '__main__':
    unittest.main(testRunner=ColorTextTestRunner(verbosity=0))
