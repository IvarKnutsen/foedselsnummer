import unittest

from foedselsnummer import generateFNr

def validate_control_digits(fnr):
    """Returns True if the control digits in an 11-digit ID are correct."""
    weights1 = [3, 7, 6, 1, 8, 9, 4, 5, 2]
    weights2 = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]

    digits = [int(c) for c in fnr]

    c1 = 11 - (sum(weights1[i] * digits[i] for i in range(9)) % 11)
    if c1 in [10, 11]:
        c1 = 0

    c2 = 11 - ((sum(weights2[i] * digits[i] for i in range(9)) + 2 * c1) % 11)
    if c2 in [10, 11]:
        c2 = 0

    return digits[9] == c1 and digits[10] == c2

class testFoedselsnummer(unittest.TestCase):
    def test_length(self):
        self.assertEqual(len(generateFNr(12, 12, 72)), 11)

    def test_digits_only(self):
        fnr = generateFNr(12, 12, 72)
        self.assertTrue(fnr.isdigit())

    def test_date_encoded_in_output(self):
        fnr = generateFNr(5, 3, 90)
        self.assertEqual(fnr[:2], "05")   # day, zero-padded
        self.assertEqual(fnr[2:4], "03")  # month, zero-padded
        self.assertEqual(fnr[4:6], "90")  # year

    def test_control_digits_valid(self):
        fnr = generateFNr(12, 12, 72)
        self.assertTrue(validate_control_digits(fnr))

    def test_random_generation_valid(self):
        fnr = generateFNr(None, None, None)
        self.assertEqual(len(fnr), 11)
        self.assertTrue(fnr.isdigit())
        self.assertTrue(validate_control_digits(fnr))

    def test_multiple_random_ids_are_valid(self):
        for _ in range(20):
            fnr = generateFNr(None, None, None)
            self.assertTrue(validate_control_digits(fnr), f"Invalid control digits in {fnr}")

if __name__ == "__main__":
    unittest.main()
