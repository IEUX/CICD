import unittest

class SimpleMath():
    def __init__():
        pass
    def addition(a,b):
        return a+b

class TestSimpleMath(unittest.TestCase):
    def testUnitaire(self):
        self.assertEqual(SimpleMath.addition(4,5), 9)
        self.assertEqual(SimpleMath.addition(1,1), 2)

    
test = TestSimpleMath()
test.testUnitaire()