import unittest
import pathlib
import importlib.util


def load_module():
    p = pathlib.Path(__file__).parent / "Largest Greatest Common Divisor.py"
    spec = importlib.util.spec_from_file_location("lgcd", str(p))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.get_k


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
        self.get_k = load_module()

    def test_k_5_7(self):
        """get_k(5, 7) -> 1"""
        self.assertEqual(self.get_k(5, 7), 1)

    def test_k_2_10(self):
        """get_k(2, 10) -> 6"""
        self.assertEqual(self.get_k(2, 10), 6)

    def test_k_100_200(self):
        """get_k(100, 200) -> 100"""
        self.assertEqual(self.get_k(100, 200), 100)

    def test_k_123_456(self):
        """get_k(123, 456) -> 210"""
        self.assertEqual(self.get_k(123, 456), 210)


if __name__ == '__main__':
    unittest.main(testRunner=ColorTextTestRunner(verbosity=0))
