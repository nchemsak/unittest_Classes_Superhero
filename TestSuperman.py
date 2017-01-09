import unittest
from superman import *

class TestSuperman(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('Set up class')
        self.superman = Superman()

    def test_SupermanIsFlyingFast(self):
        self.assertEqual(self.superman.air_speed, 1000000)

    def test_SupermanIsSwimmingFast(self):
        self.assertEqual(self.superman.water_speed, 250)

    def test_SupermanIsASuperhero(self):
        self.assertIsInstance(self.superman, Superhero)

    def test_SupermanIsAFlyingSuperhero(self):
        self.assertIsInstance(self.superman, Flying)

    def test_SupermanIsASwimmingSuperhero(self):
        self.assertIsInstance(self.superman, Swimming)

    def test_SupermanIsARunningSuperhero(self):
        self.assertIsInstance(self.superman, Running)

    def test_SupermanMustBeBulletProof(self):
        self.assertTrue(self.superman.is_bulletproof)

    def test_SupermanHasFlyMethod(self):
        self.assertIn("fly", dir(self.superman))

    def test_SupermanIsBulletProof(self):
        self.assertIn("is_bulletproof", dir(self.superman))

if __name__ == '__main__':
    unittest.main()
