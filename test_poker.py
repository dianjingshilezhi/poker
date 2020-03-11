import unittest
from Poker import poker
class Mytest(unittest.TestCase):
    def test_Straightflush(self):
        test=poker(['2H','3H','4H','5H','6H'],['3D','4D','5D','6D','7D'])
        self.assertEquals(test,'black-win')
if __name__ == '__main__':
    mytest=Mytest
