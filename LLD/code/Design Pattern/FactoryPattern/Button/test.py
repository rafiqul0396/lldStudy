import unittest

from RoundButtonFactory import RoundButtonFactory
from RoundButton import RoundButton
from button import Button
class MyTestCase(unittest.TestCase):
    def test_something(self):

        buttonfactory=RoundButtonFactory()
        round_button=buttonfactory.createButton()
        assert isinstance(round_button,Button)


if __name__ == '__main__':
    unittest.main()
