# Testing login

import unittest
from main import login


class Testing(unittest.TestCase):

    def test_lottery_login(self):
        assert login() == True, "Testing Login"
