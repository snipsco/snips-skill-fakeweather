# -*-: coding utf-8 -*-
""" Fake weather forecast skill for Snips. """

import random
from gettext import gettext as _

class WeatherCondition(object):
    """ Wrapper for weather conditions. """
    rain, wind, sun = range(3)

ANSWERS = {
    WeatherCondition.rain: {
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
    WeatherCondition.wind: {
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
    WeatherCondition.sun: {
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


class SnipsFakeWeather(object):
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
        if self.tts_service is not None:
            self.tts_service.speak(response)

    def speak_condition(self, condition, locality, date, granularity=0):
        """ Speak a random response for a given weather condition
            at a specified locality and datetime.

        :param condition: A WeatherCondition value
                          corresponding to a weather condition, e.g.
                          WeatherCondition.sun.
        :param locality: The locality of the forecast, e.g. 'Paris,fr' or
                         'Eiffel Tower'
        :type locality: string

        :param date: Time of the forecast, in ISO 8601 format, e.g.
                     "2017-07-21T10:35:29+00:00"
        :type date: datetime

        :return: A random response for a given weather condition
                 at a specified locality and datetime.
        """
        response = self.generate_condition_sentence(
            condition, locality, date, granularity)
        if self.tts_service is not None:
            self.tts_service.speak(response)

    def speak_temperature(self, locality, datetime, granularity=0):
        """ Speak a temperature response for a given weather condition
                    at a specified locality and datetime.

                :param locality: The locality of the forecast, e.g. 'Paris,fr' or
                                 'Eiffel Tower'
                :type locality: string

                :param date: Time of the forecast, in ISO 8601 format, e.g.
                             "2017-07-21T10:35:29+00:00"
                :type date: datetime

                :return: A random response for a given weather condition
                         at a specified locality and datetime.
                """
        response = SnipsFakeWeather.generate_temperature(locality, datetime, granularity)
        if self.tts_service is not None:
            self.tts_service.speak(response)

    @staticmethod
    def generate_condition_sentence(condition, locality, date, granularity=0):
        """ Generate a random response for a given weather condition
            at a specified locality and datetime.

        :param condition: A WeatherCondition value
                          corresponding to a weather condition, e.g.
                          WeatherCondition.sun.
        :type condition: SnipsFakeWeather.WeatherCondition

        :param locality: The locality of the forecast, e.g. 'Paris,fr' or
                         'Eiffel Tower'.
        :type locality: string

        :param date: Time of the forecast, in ISO 8601 format, e.g.
                     "2017-07-21T10:35:29+00:00".
        :type date: datetime

        :param granularity: The granularity of the weather forecast,
                            e.g. "tomorrow at 12.00" or "Friday".
        :type granularity: int

        :return: A random response for a given weather condition
                 at a specified locality and datetime.
        """
        if condition is None:
            return SnipsFakeWeather.generate_forecast_sentence(locality, date)

        if condition in ANSWERS:
            choice = random.choice([True, False])
            answer = random.choice(ANSWERS[condition][choice])
        else:
            return _("Sorry, we couldn't find the weather conditions")

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
    def generate_temperature(locality, date, granularity=0, use_celcius=True):
        """ Generates a temperature sentence, for an optional locality and an optional date
        with an associated optional granularity.
        :param use_celcius:
        :type use_celcius: Boolean

        :param locality:
        :type locality: String

        :param date: Time of the forecast, in ISO 8601 format, e.g. "2017-07-21T10:35:29+00:00".
        :type date: datetime

        :param granularity: The granularity of the weather forecast.
        :type granularity: int

        :rtype: string
        """
        degrees = random.choice([12, 15, 18, 21, 23])

        if use_celcius:
            degrees_sentence = _("{} degrees Celcius").format(degrees)
        else:
            degrees_sentence = _("{} degrees Fahrenheit").format(degrees)

        if locality and date:
            sentence = _("On {} in {}, it's going to be {}").format(
                SnipsFakeWeather.date_to_string(date, granularity),
                locality,
                degrees_sentence
            )

        elif locality:
            sentence = _("In {}, it's going to be {}").format(
                locality,
                degrees_sentence
            )
        elif date:
            sentence = _("On {}, it's going to be {}").format(
                SnipsFakeWeather.date_to_string(date, granularity),
                degrees_sentence
            )
        else:
            sentence = _("It's going to be {}").format(degrees_sentence)

        return sentence



    @staticmethod
    def date_to_string(date, granularity=0):
        """ Convert a date to a string, with an appropriate level of
            granularity.

        :param date: A datetime object.
        :param granularity: Granularity for the desired textual representation.
                            0: precise (date and time are returned)
                            1: day (only the week day is returned)
                            2: month (only year and month are returned)
                            3: year (only year is returned)
        :return: A textual representation of the date.
        """
        if not date:
            return None

        if granularity == 0:
            return date.strftime("%A")
        elif granularity == 1:
            return date.strftime("%A, %d")
        elif granularity == 2:
            return date.strftime("%A, %d %B")

        return date.strftime("%A, %d %B, %H:%M%p")
