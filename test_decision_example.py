import unittest
from decision_example import check_discount_eligibility

class TestCheckDiscountEligibility(unittest.TestCase):

    def test_negative_age(self):
        with self.assertRaisesRegex(ValueError, "Idade não pode ser negativa."):
            check_discount_eligibility(-1, False)
        with self.assertRaisesRegex(ValueError, "Idade não pode ser negativa."):
            check_discount_eligibility(-10, True)

    def test_senior_discount(self):
        self.assertEqual(check_discount_eligibility(60, False), "15% de desconto")
        self.assertEqual(check_discount_eligibility(65, True), "15% de desconto")
        self.assertEqual(check_discount_eligibility(99, False), "15% de desconto")

    def test_child_discount(self):
        self.assertEqual(check_discount_eligibility(10, False), "10% de desconto")
        self.assertEqual(check_discount_eligibility(17, True), "10% de desconto")
        self.assertEqual(check_discount_eligibility(0, False), "10% de desconto") # Edge case: age 0

    def test_student_discount(self):
        self.assertEqual(check_discount_eligibility(18, True), "20% de desconto")
        self.assertEqual(check_discount_eligibility(25, True), "20% de desconto")
        self.assertEqual(check_discount_eligibility(59, True), "20% de desconto")

    def test_no_discount(self):
        self.assertEqual(check_discount_eligibility(18, False), "Sem desconto")
        self.assertEqual(check_discount_eligibility(30, False), "Sem desconto")
        self.assertEqual(check_discount_eligibility(59, False), "Sem desconto")

if __name__ == '__main__':
    unittest.main()

