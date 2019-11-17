import unittest
import weather_model

class Test_Weather(unittest.TestCase):

    def test_LocationSearch(self):
        self.assertEqual(weather_model.LocationSearch('Bangalore'), ['Success', 'Bangalore', 'IN', 1277333])
        self.assertEqual(weather_model.LocationSearch('New Delhi'), ['Success', 'New Delhi', 'IN', 1261481])
        self.assertEqual(weather_model.LocationSearch('Ahmedabad'), ['Failed', 'Ahmedabad'])
        self.assertEqual(weather_model.LocationSearch('Allahabad'), ['Success', 'Allahabad', 'IN', 1278994])

if __name__ == "__main__":
    unittest.main()  