# -*-: coding utf-8 -*-
""" Fake weather forecast skill for Snips. """

import random
from gettext import gettext as _
from enum import Enum


class WeatherCondition(Enum):
    """ Wrapper for weather conditions. """
    RAIN = 1
    WIND = 2
    SUN = 3

ANSWERS = {
    WeatherCondition.RAIN: {
        True: [
            _("Yes, it is going to be raining heavily"),
            _("Yes, you can expect rain showers"),
            _("Yes, thunderstorm and heavy rain is expected"),
            _("Yes, light rain is expected"),
            _("Yes, it is going to be rainy and windy")
        ],
        False: [
            _("No, expected dry weather"),
            _("No, rain is not expected"),
            _("No, it is going to be sunny and dry")
        ]
    },
    WeatherCondition.WIND: {
        True: [
            _("Yes, it is going to be windy"),
            _("Yes, strong winds are expected"),
            _("Yes, winds and thunderstorms are expected"),
        ],
        False: [
            _("No, wind will be still"),
            _("No, it is not going to be windy")
        ]
    },
    WeatherCondition.SUN: {
        True: [
            _("Yes, it is going to be sunny"),
            _("Yes, clear sky is expected"),
            _("Yes, sun and light wind"),
            _("Yes, it is going to be sunny and hot"),
        ],
        False: [
            _("No, it is going to be cloudy"),
            _("No, rain and thunderstorm is expected"),
            _("No, expect rain showers"),
            _("No, it is not going to be sunny"),
        ]
    }
}


class SnipsFakeWeather:
    """ Skill for presenting fake weather forecasts. """

    def __init__(self, tts_service=None):
        """
        :param tts_service: A TTS service, i.e. an object which has a
                            `speak(text)` method for speaking the result.
        """
        self.tts_service = tts_service

    def speak_forecast(self, locality, date, granularity=0):
        """ Speak a random weather forecast at a specified locality and
            datetime.

        :param locality: The locality of the forecast, e.g. 'Paris,fr' or
                         'Eiffel Tower'
        :param date: Time of the forecast, in ISO 8601 format, e.g.
                     "2017-07-21T10:35:29+00:00"
        :param granularity: The granularity of the weather forecast,
                            e.g. "tomorrow at 12.00" or "Friday".
        :return: A random response for a given weather condition
                 at a specified locality and datetime.
        """
        response = SnipsFakeWeather.generate_forecast_sentence(
            locality, date, granularity)
        if self.tts_service:
            self.tts_service.speak(response)

    def speak_condition(self, condition, locality, date, granularity=0):
        """ Speak a random response for a given weather condition
            at a specified locality and datetime.

        :param condition: A SnipsFakeWeather.WeatherCondition enum
                          corresponding to a weather condition, e.g.
                          SnipsFakeWeather.WeatherCondition.SUN.
        :param locality: The locality of the forecast, e.g. 'Paris,fr' or
                         'Eiffel Tower'
        :param date: Time of the forecast, in ISO 8601 format, e.g.
                     "2017-07-21T10:35:29+00:00"
        :return: A random response for a given weather condition
                 at a specified locality and datetime.
        """
        response = self.generate_condition_sentence(
            condition, locality, date, granularity)
        if self.tts_service:
            self.tts_service.speak(response)

    @staticmethod
    def generate_condition_sentence(condition, locality, date, granularity=0):
        """ Generate a random response for a given weather condition
            at a specified locality and datetime.

        :param condition: A SnipsFakeWeather.WeatherCondition enum
                          corresponding to a weather condition, e.g.
                          SnipsFakeWeather.WeatherCondition.SUN.
        :param locality: The locality of the forecast, e.g. 'Paris,fr' or
                         'Eiffel Tower'.
        :param date: Time of the forecast, in ISO 8601 format, e.g.
                     "2017-07-21T10:35:29+00:00".

        :param granularity: The granularity of the weather forecast,
                            e.g. "tomorrow at 12.00" or "Friday".
        :return: A random response for a given weather condition
                 at a specified locality and datetime.
        """
        if not condition:
            return SnipsFakeWeather.generate_forecast_sentence(locality, date)

        if condition in ANSWERS:
            choice = random.choice([True, False])
            answer = random.choice(ANSWERS[condition][choice])
        else:
            answer = _("Sorry, we couldn't find the weather conditions")

        if locality and date:
            sentence = _("{} {} in {}").format(answer,
                                               SnipsFakeWeather.date_to_string(
                                                   date, granularity),
                                               locality)
        elif locality:
            sentence = _("{} in {}").format(answer, locality)
        elif date:
            sentence = _("{} {}").format(
                answer, SnipsFakeWeather.date_to_string(date, granularity))
        else:
            sentence = answer
        return sentence

    @staticmethod
    def generate_forecast_sentence(locality, date, granularity=0):
        """ Speak a random weather forecast at a specified locality and
            datetime.

        :param locality: The locality of the forecast, e.g. 'Paris,fr' or
                         'Eiffel Tower'.
        :param date: Time of the forecast, in ISO 8601 format, e.g.
                     "2017-07-21T10:35:29+00:00".
        :param granularity: The granularity of the weather forecast,
                            e.g. "tomorrow at 12.00" or "Friday".
        :return: A random forecast for a given weather condition
                 at a specified locality and datetime.
        """
        if locality and date:
            date_s = SnipsFakeWeather.date_to_string(date, granularity)
            description = _("Weather conditions for " +
                            "{} for {}").format(locality, date_s)
        elif locality:
            description = _(
                "Current weather conditions for {}").format(locality)
        elif date:
            description = _("Weather conditions for {}").format(
                SnipsFakeWeather.date_to_string(date, granularity))
        else:
            description = _("Current weather conditions")
        return "{0}: {1}".format(description,
                                 SnipsFakeWeather.generate_random_forecast())

    @staticmethod
    def generate_random_forecast(use_celcius=True):
        """ Generate a random weather forecast.

        :param use_celcius: If true, phrase should use degrees celcius,
                            otherwise use Fahrenheit.
        :return: A phrase describing a random weather forecast.
        """
        degrees = random.choice([12, 15, 18, 21, 23])
        conditions = random.choice([_("cloudy"), _("rainy"), _(
            "thunder storms"), _("windy"), _("clear sky"), _("light wind")])
        if use_celcius:
            degrees_sentence = _("{} degrees celcius").format(degrees)
        else:
            degrees = int(degrees * 9 / 5 + 32)
            degrees_sentence = _("{} degrees Fahrenheit").format(degrees)
        return _("{}, {}").format(conditions, degrees_sentence)

    @staticmethod
    def date_to_string(date, granularity=0):
        """ Convert a date to a string, with an appropriate level of
            granularity.

        :param date: A datetime object.
        :param granularity: Granularity for the desired textual representation.
                            0: precise (date and time are returned)
                            1: day (only date is returned)
                            2: month (only year and month are returned)
                            4: year (only year is returned)
        :return: A textual representation of the date.
        """
        if not date:
            return None
        if granularity == 0:
            return date.strftime("%A, %d %b, %H:%M%p")
        else:
            return date.strftime("%A, %d %b")
