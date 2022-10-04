def factoriel(n):
    if n==0:
        return 1
    else:
        return n*factoriel(n-1)

print(factoriel(5))

from unittest import TestCase
from factoriel import factoriel

class Test(TestCase):
    def test_factoriel(self):
        self.assertEqual(1, factoriel(0))
        self.assertEqual(24, factoriel(4))
