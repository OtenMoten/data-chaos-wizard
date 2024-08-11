import unittest
import sys
import os

# 🧙‍♂️ Enchant our vision to see the mystical 'src' realm
# (Add the src directory to the Python path)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# 🔮 The Grand Test Ritual begins!
if __name__ == '__main__':
    # 🕵️‍♂️ Summon the Test Seeker to find all our magical trials
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')

    # 🏃‍♂️ Call upon the Test Runner, a swift messenger of results
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)

    # 📜 Declare the outcome of our trials to the kingdom (exit code)
    sys.exit(not result.wasSuccessful())
