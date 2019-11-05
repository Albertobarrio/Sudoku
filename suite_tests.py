import unittest
import test_api
import test_interface
import test_sudoku


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromModule(test_api))
    suite.addTest(loader.loadTestsFromModule(test_interface))
    suite.addTest(loader.loadTestsFromModule(test_sudoku))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite())
