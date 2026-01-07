import unittest
import pathlib
import sys


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


def main():
    start_dir = pathlib.Path(__file__).parent
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=str(start_dir), pattern='test_*.py')
    runner = ColorTextTestRunner(verbosity=0)
    result = runner.run(suite)

    total = result.testsRun
    failures = len(result.failures) + len(result.errors)

    print()
    if failures == 0:
        print(f'All tests passed ({total}/{total})')
    else:
        print(f'Passed: {total - failures}/{total} — Failures: {failures}')

    sys.exit(0 if failures == 0 else 1)


if __name__ == '__main__':
    main()
