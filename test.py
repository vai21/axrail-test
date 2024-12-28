import unittest

from scripts import cheapest_flight

class TestCheapFlight(unittest.TestCase):
    def test_cheap_flight_1(self):
        """
        Test cheap flight result with input case1.json
        :return: integer
        """
        data = "case1.json"
        result = cheapest_flight(data)
        self.assertEqual(result, 700)
    def test_cheap_flight_2(self):
        """
        Test cheap flight result with input case2.json
        :return: integer
        """
        data = "case2.json"
        result = cheapest_flight(data)
        self.assertEqual(result, 200)
    def test_cheap_flight_3(self):
        """
        Test cheap flight result with input case3.json
        :return: integer
        """
        data = "case3.json"
        result = cheapest_flight(data)
        self.assertEqual(result, 500)

if __name__ == '__main__':
    unittest.main()
