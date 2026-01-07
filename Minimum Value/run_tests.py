import unittest
import pathlib
import sys


def main():
    start_dir = pathlib.Path(__file__).parent
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=str(start_dir), pattern='test_*.py')
    runner = unittest.TextTestRunner(verbosity=2)
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
