"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data


# Part 1: vowel_count
def vowel_count(text: str) -> int:
    # TODO: Purpose: Count the vowels in a string
    # TODO: Input(s): The text is the string being checked
    # TODO: Output: The number of vowels including uppercase vowels
    count = 0

    for letter in text:
        if letter.lower() in "aeiou":
            count = count + 1

    return count

# Part 2: short_lists
def short_lists(items: list[list[int]]) -> list[list[int]]:
    # TODO: Purpose: find nested lists containing 2 elements
    # TODO: Input(s): items is a list of integers
    # TODO: Output: new list containing matching nested lists
    result = []

    for item in items:
        if len(item) == 2:
            result.append(item)

    return result


# Part 3: ascending_pairs
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    # TODO: Purpose: put each pair in ascending order
    # TODO: Input(s): items is a list of lists of integers
    # TODO: Output: new list of pairs ordered from small to large
    result = []
    for item in items:
        if len(item) == 2:
            if item[0] > item[1]:
                result.append([item[1], item[0]])
            else:
                result.append([item[0], item[1]])
        else:
            result.append(item)

    return result

# Part 4: add_prices
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    # TODO: Purpose: add 2 prices together
    # TODO: Input(s): first and second are price objects
    # TODO: Output: new price object with total dollars and cents
    total_cents = first.cents + second.cents

    dollars = first.dollars + second.dollars
    dollars = dollars + total_cents // 100

    cents = total_cents % 100

    return data.Price(dollars, cents)

# Part 5: rectangle_area
def rectangle_area(rectangle: data.Rectangle) -> float:
    # TODO: Purpose: calculate the area of a rectangle
    # TODO: Input(s): rectangle is a Rectangle object
    # TODO: Output: area of the rectangle
    width = rectangle.bottom_right.x - rectangle.top_left.x
    height = rectangle.top_left.y - rectangle.bottom_right.y

    area = width * height

    return area


# Part 6: books_by_author
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    # TODO: Purpose: find books written by a specific author
    # TODO: Input(s): author is a name and books is a list of Book objects
    # TODO: Output: A list of Book objects written by that author
    result = []

    for book in books:
        if author in book.authors:
            result.append(book)

    return result


# Part 7: circle_bound
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    # TODO: Purpose: create the smallest circle enclosing a rectangle
    # TODO: Input(s): rectangle is a Rectangle object
    # TODO: Output: a new Circle object with center and radius
    x1 = rectangle.top_left.x
    y1 = rectangle.top_left.y

    x2 = rectangle.bottom_right.x
    y2 = rectangle.bottom_right.y

    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2

    center = data.Point(center_x, center_y)

    radius = ((x2 - center_x) ** 2 +
              (y2 - center_y) ** 2) ** 0.5

    return data.Circle(center, radius)


# Part 8: below_pay_average
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    # TODO: Purpose: find employees earning less than average pay.
    # TODO: Input(s): employees is a list of Employee objects.
    # TODO: Output: list of names of employees below the average.
    if len(employees) == 0:
        return []

    total = 0

    for employee in employees:
        total = total + employee.pay_rate

    average = total / len(employees)

    result = []

    for employee in employees:
        if employee.pay_rate < average:
            result.append(employee.name)

    return result
