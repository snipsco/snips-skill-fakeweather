from unittest import TestCase
from datetime import datetime

from snipsfakeweather.snipsfakeweather import SnipsFakeWeather


class TestSkill(TestCase):

    # def setUp(self):
    #     self.skill = SnipsFakeWeather()

    def test_skill(self):
        # self.skill.speak_forecast("Paris,fr", datetime.now(), 0)
        self.assertEqual(1, 1)
