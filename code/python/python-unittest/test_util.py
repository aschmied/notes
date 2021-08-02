# Tests for the `util` module. These tests describe the behaviour
# of `util`.

# To run them:

# 1. Place "util.py" and "test_util.py" side-by-side in a
#    directory.
# 2. `cd` to that directory.
# 3. Run the following command:
#    python -m unittest test_util.py
#    This tells python to run the `unittest` module with
#    "test_util.py" as input.

# Import the unittest module followed by the module under test.
import unittest

import util

# If you need other modules to set up your tests, import them here.

# A test case class. It is named after the module or class it is
# testing. Here we are testing the util module, so it is TestUtil.
# It must extend unittest.TestCase. You can have multiple test
# case classes in one file if you want.
class TestUtil(unittest.TestCase):
    # Names that beging with "test" are the tests. Each of these
    # methods will be executed by the test runner. You will usually
    # name them for the method and situation you are testing. In
    # this case I am testing the "reverse" method for an empty list.
    def test_reverse_empty_list(self):
        self.assertListEqual(util.reverse([]), [])

    # unittest.TestCase includes methods to test your error handling.
    # Here we ensure that an exception is thrown if we pass None to
    # the "reverse" method.
    def test_reverse_none(self):
        with self.assertRaises(TypeError):
            util.reverse(None)

    def test_reverse_nonempty_list(self):
        self.assertListEqual(util.reverse(['blah', 'blerg']), ['blerg', 'blah'])
