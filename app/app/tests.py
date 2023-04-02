"""
Sample Test
"""


from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase): 
    """Test the calc module."""
    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(5, 7)

        self.assertEqual(res, 12)

    def test_substract_numbers(self):
        """Test substracting numbers."""
        res = calc.substract(15, 10)

        self.assertEqual(res, 5)
