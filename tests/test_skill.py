from unittest import TestCase

from snipsfakeweather.snipsfakeweather import SnipsFakeWeather


class TestSkill(TestCase):

    def setUp(self):
        self.skill = SnipsFakeWeather()

    def test_skill(self):
        self.skill.execute()
        self.assertEqual(1, 1)
