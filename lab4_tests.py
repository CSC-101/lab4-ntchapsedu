import data
import lab4
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)

    def test_first_element_1_1(self):
        input = [[8, 9], [4, 5]]
        result = lab4.first_element(input)
        expected = [8, 4]
        self.assertEqual(expected, result)


    # Part 2
    def test_first_element_2(self):
        input = [data.Point(1,2),data.Point(2,3),data.Point(4,5),data.Point(6,7)]
        result = lab4.x_coordinates(input)
        expected = [1,2,4,6]
        self.assertEqual(expected, result)
    def test_first_element_2_2(self):
        input = [data.Point(5,2),data.Point(4,3),data.Point(-1,5),data.Point(9,7)]
        result = lab4.x_coordinates(input)
        expected = [5,4,-1,9]
        self.assertEqual(expected, result)


    # Part 3
    def test_first_element_3(self):
        input = [data.Point(1, 1), data.Point(-1, 1), data.Point(-1, -1), data.Point(-1, 1)]
        result = lab4.are_in_positive_quadrant(input)
        expected = [[1, 1]]
        self.assertEqual(expected, result)

    def test_first_element_3(self):
        input = [data.Point(2, -2), data.Point(5, -1), data.Point(-1, -1), data.Point(101, 2)]
        result = lab4.are_in_positive_quadrant(input)
        expected = [[101, 2]]
        self.assertEqual(expected, result)


   # Part 4
    def test_first_element_4(self):
        input = [data.Point(1, 1), data.Point(2, 2)]
        result = lab4.distance(input)
        expected = 1.41
        self.assertEqual(expected, result)

    def test_first_element_4_2(self):
        input = [data.Point(4, 1), data.Point(5, 8)]
        result = lab4.distance(input)
        expected = 7.07
        self.assertEqual(expected, result)
    # Part 5
    def test_first_element_5(self):
        input = [data.Point(1, 1), data.Point(2, 2)]
        result = lab4.manhattan_distance(input)
        expected =  2
        self.assertEqual(expected, result)

    def test_first_element_5_5(self):
        input = [data.Point(1, 3), data.Point(4,4)]
        result = lab4.manhattan_distance(input)
        expected = 4
        self.assertEqual(expected, result)


    # Part 6
    def test_first_element_6(self):
        input = [data.Point(1, 1)]
        result = lab4.distance_all(input)
        expected = 1.41
        self.assertEqual(expected, result)

    def test_first_element_6(self):
        input = [data.Point(3, 4)]
        result = lab4.distance_all(input)
        expected = 5.0
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
