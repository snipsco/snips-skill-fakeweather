#!/usr/bin/env python3
# encoding: utf-8

import datetime
import random
from gettext import gettext as _


class SnipsFakeWeather:

    class WeatherCondition:
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

    def __init__(self, tts_service=None):
        self.tts_service = tts_service

    def speak_forecast(self, locality, datetime, granularity=0):
        response = self.generate_forecast_sentence(locality, datetime)
        if self.tts_service:
            print("[fakeweather] " + response)
            self.tts_service.speak(response)

    def speak_condition(self, condition, locality, datetime, granularity=0):
        response = self.generate_condition_sentence(
            condition, locality, datetime)
        if self.tts_service:
            print("[fakeweather] " + response)
            self.tts_service.speak(response)

    def generate_forecast_sentence(self, locality, datetime, granularity=0):
        """ Generate a random weather forecast at a specified locality and
            datetime.

        :param locality: The locality of the forecast, e.g. 'Paris,fr' or
                         'Eiffel Tower'
        :param datetime: Time of the forecast, in ISO 8601 format, e.g.
                         "2017-07-21T10:35:29+00:00"
        :return: A random response for a given weather condition
                 at a specified locality and datetime.
        """
        if locality and datetime:
            description = _("Weather conditions for {} for {}").format(locality,
                                                                       DateUtils.to_string(datetime, granularity))
        elif locality:
            description = _(
                "Current weather conditions for {}").format(locality)
        elif datetime:
            description = _("Weather conditions for {}").format(
                DateUtils.to_string(datetime, granularity))
        else:
            description = _("Current weather conditions")
        return "{0}: {1}".format(description, self.generate_random_forecast())

    def generate_condition_sentence(self, condition, locality, datetime, granularity=0):
        """ Generate a random response for a given weather condition
            at a specified locality and datetime.

        :param condition: A SnipsFakeWeather.WeatherCondition enum
                          corresponding to a weather condition, e.g.
                          SnipsFakeWeather.WeatherCondition.sun.
        :param locality: The locality of the forecast, e.g. 'Paris,fr' or
                         'Eiffel Tower'
        :param datetime: Time of the forecast, in ISO 8601 format, e.g.
                         "2017-07-21T10:35:29+00:00"
        :return: A random response for a given weather condition
                 at a specified locality and datetime.
        """
        if not condition:
            return self.generate_forecast_sentence(locality, datetime)

        yesNo = random.choice([True, False])
        if condition in self.phrases:
            answer = random.choice(self.phrases[condition][yesNo])
        else:
            answer = _("Sorry, we couldn't find the weather conditions")

        datetime_s = DateUtils.to_string(datetime) if isinstance(
            datetime, DateTimeRepr) else None

        if locality and datetime:
            sentence = _("{} {} in {}").format(answer,
                                               DateUtils.to_string(
                                                   datetime, granularity),
                                               locality)
        elif locality:
            sentence = _("{} in {}").format(answer, locality)
        elif datetime:
            sentence = _("{} {}").format(
                answer, DateUtils.to_string(datetime, granularity))
        else:
            sentence = answer
        return sentence

    def generate_random_forecast(self, use_celcius=True):
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


class DateUtils:

    @staticmethod
    def to_string(datetime, granularity=0):
        """ Convert a datetime to a string, with an appropriate level of
            granularity.

        :param datetime: A datetime object.
        :param granularity: Granularity for the desired textual representation.
                            0: precise (date and time are returned)
                            1: day (only date is returned)
                            2: month (only year and month are returned)
                            4: year (only year is returned)
        :return: A textual representation of the datetime.
        """
        if not datetime:
            return None
        if granularity == 0:
            return datetime.strftime("%A, %d %b, %H:%M%p")
        else:
            return datetime.strftime("%A, %d %b")
