import unittest
from grade_calculator import calculate_average_grade

class TestCalculateAverageGrade(unittest.TestCase):

    def test_empty_list(self):
        with self.assertRaisesRegex(ValueError, "A lista de notas não pode estar vazia."):
            calculate_average_grade([])

    def test_invalid_type(self):
        with self.assertRaisesRegex(TypeError, "Todas as notas devem ser números."):
            calculate_average_grade([10, "a", 7])

    def test_out_of_range_low(self):
        with self.assertRaisesRegex(ValueError, "As notas devem estar entre 0 e 10."):
            calculate_average_grade([10, -1, 7])

    def test_out_of_range_high(self):
        with self.assertRaisesRegex(ValueError, "As notas devem estar entre 0 e 10."):
            calculate_average_grade([10, 11, 7])

    def test_valid_grades(self):
        self.assertEqual(calculate_average_grade([10, 8, 9, 7, 6]), 8.0)
        self.assertEqual(calculate_average_grade([5, 5, 5, 5, 5]), 5.0)
        self.assertEqual(calculate_average_grade([10, 10, 10]), 10.0)
        self.assertEqual(calculate_average_grade([0, 0, 0]), 0.0)
        self.assertAlmostEqual(calculate_average_grade([7.5, 8.5, 9.5]), 8.5)

if __name__ == '__main__':
    unittest.main()
