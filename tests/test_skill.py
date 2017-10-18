from unittest import TestCase
from datetime import datetime

from snipsfakeweather.snipsfakeweather import SnipsFakeWeather
from snipsfakeweather.snipsfakeweather import WeatherCondition

class BaseTest(TestCase):

    def setUp(self):
        self.skill = SnipsFakeWeather(None)

class ConditionTest(BaseTest):

    def test_generate_condition_with_correct_params(self):
        condition = WeatherCondition.rain
        locality = "Tokyo"
        date = datetime.now()
        granularity = 1

        result = self.skill.generate_condition_sentence(condition, locality, date, granularity)
        self.assertGreater(len(result), 0)

    def test_generate_condition_with_wrong_condition(self):
        condition = "FAKE_CONDITION"
        locality = "New York"
        date = datetime.now()
        granularity = 1

        result = self.skill.generate_condition_sentence(condition, locality, date, granularity)
        self.assertEqual(result, "Sorry, we couldn't find the weather conditions")

    def test_generate_condition_without_locality_nor_date(self):
        condition = WeatherCondition.sun

        result = self.skill.generate_condition_sentence(condition,
                                                        locality=None,
                                                        date=None,
                                                        granularity=1)

        self.assertGreater(len(result), 0)



class ForecastTest(BaseTest):

    def test_generate_forecast_with_correct_params(self):
        locality = "Bishkek"
        date = datetime.now()
        result = self.skill.generate_forecast_sentence(locality, date)

        self.assertGreater(len(result), 0)

    def test_generate_forecast_without_location(self):
        result = self.skill.generate_forecast_sentence(locality=None, date=datetime.now())
        self.assertGreater(len(result), 0)

    def test_generate_forecast_without_date(self):
        result = self.skill.generate_forecast_sentence(locality="Paris", date=None)
        self.assertIn("Paris", result)

    def test_generate_forecast_without_date_nor_location(self):
        result = self.skill.generate_forecast_sentence(locality=None, date=None)
        self.assertGreater(len(result), 0)


class TemperatureTest(BaseTest):

    def test_generate_forecast_with_correct_params(self):
        locality = "Bishkek"
        date = datetime.now()
        result = self.skill.generate_temperature(locality=locality, date=date, granularity=0)
        self.assertGreater(len(result), 0)

    def test_generate_forecast_without_parameters(self):
        result = self.skill.generate_temperature(None, None, granularity=0)
        self.assertGreater(len(result), 0)