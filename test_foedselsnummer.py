import unittest

from foedselsnummer import generateFNr

class testFoedselsnummer(unittest.TestCase):
    def test_string(self):
        self.assertTrue("generateFNr(12,12,72)".isalpha)

if __name__ == "__main__":
    unittest.main()