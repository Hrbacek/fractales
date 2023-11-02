"""TDD practice for rewriting systems"""
import unittest
from src.fractal_gen import _rewrite

class rewritingTest(unittest.TestCase):
    """TDD practice for rewriting systems"""
    def test_rewriteOneSimbolOneTime(self):
        """Test
        """
        rules = {"X": "X"}
        string = "X"
        assert _rewrite(string=string, rules=rules, times=1) == "X"

    def test_rewriteSimbolOneTime(self):
        """Test
        """
        rules = {"X": "X-X"}
        string = "XX"
        r = _rewrite(
            string=string,
            rules=rules,
            times=1
        )
        assert r == "X-XX-X"

    def test_rewriteSimbolTwoTimes(self):
        """Test
        """
        rules = {"X": "X-X"}
        string = "XX"
        r = _rewrite(
            string=string,
            rules=rules,
            times=2
        )
        assert r == "X-X-X-XX-X-X-X"

    def test_rewriteTwoSimbolsOneTime(self):
        """Test
        """
        rules = {"X": "X-X", "G": "G+X"}
        string = "XG"
        r = _rewrite(
            string=string,
            rules=rules,
            times=1
        )
        assert r == "X-XG+X"

    def test_rewriteTwoSimbolsOneTime2(self):
        """Test
        """
        rules = {"X": "X-X", "G": "G+X"}
        string = "GXG"
        r = _rewrite(
            string=string,
            rules=rules,
            times=1
        )
        assert r == "G+XX-XG+X"

    def test_rewriteTwoSimbolsTwoTimes(self):
        """Test
        """
        rules = {"X": "X-X", "G": "G+X"}
        string = "XG"
        r = _rewrite(
            string=string,
            rules=rules,
            times=2
        )
        assert r == "X-X-X-XG+X+X-X"

    def test_rewriteTwoSimbolsTwoTimes2(self): #V1 for the code implementation
        """Test
        """
        rules = {"X": "X-G", "G": "G+X"}
        string = "GXG"
        r = _rewrite(
            string=string,
            rules=rules,
            times=2
        )
        assert r == "G+X+X-GX-G-G+XG+X+X-G"

    def test_rewriteMultipleSimbolsOneTime(self):
        """Test
        """
        rules = {"A": "Ba", "B": "bA", "a": "A", "b": "B"}
        string = "A"
        r = _rewrite(
            string=string,
            rules=rules,
            times=1
        )
        assert r == "Ba"

    def test_rewriteMultipleSimbolsTwoTimes(self):
        """Test
        """
        rules = {"A": "Ba", "B": "bA", "a": "A", "b": "B"}
        string = "A"
        r = _rewrite(
            string=string,
            rules=rules,
            times=2
        )
        assert r == "bAA"

    def test_rewriteMultipleSimbolsMultipleTimes(self):
        """Test
        """
        rules = {"A": "Ba", "B": "bA", "a": "A", "b": "B"}
        string = "A"
        r = _rewrite(
            string=string,
            rules=rules,
            times=4
        )
        assert r == "bAbAAbAA"

if __name__ == '__main__':
    unittest.main()
