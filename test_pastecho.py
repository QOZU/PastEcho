# test_pastecho.py
"""
Tests for PastEcho module.
"""

import unittest
from pastecho import PastEcho

class TestPastEcho(unittest.TestCase):
    """Test cases for PastEcho class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PastEcho()
        self.assertIsInstance(instance, PastEcho)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PastEcho()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
