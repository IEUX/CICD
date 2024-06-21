"""Test class for simpleMaths"""

import maths

class TestSimpleMath():
    """Test"""
    def test_add(self):
        """"Test Add"""
        assert maths.SimpleMath().addition(4,5) ==  9
        assert maths.SimpleMath().addition(1,1) == 2
    def test_sub(self):
        """"Test Sub"""
        assert maths.SimpleMath().substract(5,1) == 4
        assert maths.SimpleMath().substract(0,1) == -1
