import maths

class TestSimpleMath():
    def testAdd(self):
        assert maths.SimpleMath.addition(4,5) ==  9
        assert maths.SimpleMath.addition(1,1) == 2
    def testSub(self):
        assert maths.SimpleMath.substract(5,1) == 4
        assert maths.SimpleMath.substract(0,1) == -1
