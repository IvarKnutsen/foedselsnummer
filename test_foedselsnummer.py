import unittest

from foedselsnummer import generateFNr

class testFoedselsnummer(unittest.TestCase):
    def test_string(self):
        self.assertTrue("generateFNr(12,12,72)".isalpha)
    def test_length(self):
        self.assertTrue(len(generateFNr(12,12,72)) == 11)

if __name__ == "__main__":
    unittest.main()