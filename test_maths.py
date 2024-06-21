import maths

class TestSimpleMath():
    def testUnitaire(self):
        assert maths.SimpleMath.addition(4,5) ==  9
        assert maths.SimpleMath.addition(1,1) == 2