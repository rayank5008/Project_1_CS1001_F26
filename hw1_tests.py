"""CSC 1001 - Programming Assignment 1: student-written unit tests.

Create at least TWO separate, meaningful unit tests for each function.
The sixteen methods below are ONLY PLACEHOLDERS: they are not real tests.

Replace each self.fail(...) with test inputs, a call to the appropriate
hw1 function, and unittest assertions about its expected output.
Use methods like self.assertEqual(...) or self.assertAlmostEqual(...).

IMPORTANT: The initial test failures are intentional until you write tests
and implement the functions in hw1.py. Do not simply delete the tests.
"""

import unittest

import data
import hw1


class TestHomework1(unittest.TestCase):

    # Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
        result = hw1.vowel_count("Apple")
        self.assertEqual(result, 2)

        result = hw1.vowel_count("AEIOU")
        self.assertEqual(result, 5)

    def test_vowel_count_empty_string(self):
        result = hw1.vowel_count("")
        self.assertEqual(result, 0)

    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        items = [[1], [2, 3], [], [4, 5, 6], [7, 8]]
        result = hw1.short_lists(items)
        self.assertEqual(result, [[2, 3], [7, 8]])

    def test_short_lists_no_matching_lengths(self):
        items = [[1], [], [2, 3, 4]]
        result = hw1.short_lists(items)
        self.assertEqual(result, [])

    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        items = [[9, 2], [3, 1, 2], [5, 5]]
        result = hw1.ascending_pairs(items)
        self.assertEqual(result, [[2, 9], [3, 1, 2], [5, 5]])

    def test_ascending_pairs_other_lengths_unchanged(self):
        items = [[1], [3, 2, 1], [], [2, 8]]
        result = hw1.ascending_pairs(items)
        self.assertEqual(result, [[1], [3, 2, 1], [], [2, 8]])

    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        first = data.Price(2, 25)
        second = data.Price(3, 40)

        result = hw1.add_prices(first, second)

        self.assertEqual(result, data.Price(5, 65))
        self.assertIsNot(result, first)

    def test_add_prices_with_cents_carry(self):
        first = data.Price(3, 75)
        second = data.Price(2, 50)

        result = hw1.add_prices(first, second)

        self.assertEqual(result, data.Price(6, 25))

    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
        rectangle = data.Rectangle(
            data.Point(0, 4),
            data.Point(6, 0)
        )

        result = hw1.rectangle_area(rectangle)

        self.assertAlmostEqual(result, 24)

    def test_rectangle_area_negative_coordinates(self):
        rectangle = data.Rectangle(
            data.Point(-5, 4),
            data.Point(-1, -2)
        )

        result = hw1.rectangle_area(rectangle)

        self.assertAlmostEqual(result, 24)

    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        book1 = data.Book(["Ana", "Ben"], "First")
        book2 = data.Book(["Ben"], "Second")
        book3 = data.Book(["Ana"], "Third")

        books = [book1, book2, book3]

        result = hw1.books_by_author("Ana", books)

        self.assertEqual(result, [book1, book3])
        self.assertIs(result[0], book1)

    def test_books_by_author_no_matches(self):
        book = data.Book(["Ana"], "First")

        result = hw1.books_by_author("Jordan", [book])

        self.assertEqual(result, [])

    # Part 7: circle_bound
    def test_circle_bound_square(self):
        rectangle = data.Rectangle(
            data.Point(0, 2),
            data.Point(2, 0)
        )

        result = hw1.circle_bound(rectangle)

        self.assertEqual(result.center, data.Point(1, 1))
        self.assertAlmostEqual(result.radius, 2 ** 0.5)

    def test_circle_bound_non_square_rectangle(self):
        rectangle = data.Rectangle(
            data.Point(0, 4),
            data.Point(6, 0)
        )

        result = hw1.circle_bound(rectangle)

        self.assertEqual(result.center, data.Point(3, 2))
        self.assertAlmostEqual(result.radius, 13 ** 0.5)

    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        employees = [
            data.Employee("Alex", 10),
            data.Employee("Sam", 20),
            data.Employee("Jordan", 30)
        ]

        result = hw1.below_pay_average(employees)

        self.assertEqual(result, ["Alex"])

    def test_below_pay_average_empty_list(self):
        result = hw1.below_pay_average([])

        self.assertEqual(result, [])
        
if __name__ == '__main__':
    unittest.main()
