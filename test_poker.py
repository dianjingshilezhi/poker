import unittest
from Poker import poker
class Mytest(unittest.TestCase):
    def test_Straightflush(self):
        test=poker(['2H','3H','4H','5H','6H'],['3D','4D','5D','6D','7D'])
        self.assertEquals(test,'black-win')
    def test_4same(self):
        test=poker(['3D','4D','5D','6D','7D'],['3D','3S','3H','3C','KS'])
        self.assertEquals(test,'white-win')
    def testhulu(self):
        test=poker(['3D','3S','3H','7D','7H'],['5D','6D','9D','QD','KD'])
        self.assertEquals(test,'white-win')
    def test_santioa(self):
        test=poker(['3D','3S','3H','7D','9H'],['5D','5H','9D','9H','KD'])
        self.assertEquals(test,'white-win')
    def test_twopair(self):
        test=poker(['3D','3S','6H','7D','9H'],['5D','5H','9D','9H','KD'])
        self.assertEquals(test,'black-win')
    def test_pair(self):
        test = poker(['3D', '3S', '6H', '9D', 'QC'], ['2H', '6C', '9D', 'JH', 'KD'])
        self.assertEquals(test, 'white-win')
    def testtie(self):
        test=poker(['3H','3D','5S','9C','KD'],['3H','3D','5S','9C','KD'])
        self.assertEquals(test,'tie')
if __name__ == '__main__':
    mytest=Mytest
