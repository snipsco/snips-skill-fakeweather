#!/usr/bin/env python3
# encoding: utf-8

class SnipsFakeWeather:

    ANSWERS = {
        "rain": {
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
        "wind": {
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
        "sun": {
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

    def __init__(self, tts_service):
        self.tts_service = tts_service

    def speak_forecast(self, locality):
        response = self.generate_search_weather_forecast_response(
            locality, intent.weatherForecastStartDatetime)
        if response and self.tts_service:
            tts_service.speak(response)

    def __handle_search_weather_forecast_condition(self, intent):
        condition = intent.weatherForecastConditionName
        datetime = intent.weatherForecastStartDatetime
        locality = intent.weatherForecastLocality or intent.weatherForecastCountry or intent.weatherForecastRegion or intent.weatherForecastGeographicalPOI
        response = self.__generate_search_weather_forecast_condition_response(
            condition, locality, intent.weatherForecastStartDatetime)
        if response:
            print("[WEATHER] TTS: " + response)
            TTS.speak(response, self.locale_id, self.threading)

    ###########################################################################
    # Sentence generation
    ###########################################################################

    def __generate_search_weather_forecast_response(self, locality, datetime):
        datetime_s = DateUtils.to_string(datetime) if isinstance(
            datetime, DateTimeRepr) else None
        if locality and datetime_s:
            description = _("Weather conditions for {locality} for {datetime}").format(
                locality=locality, datetime=datetime_s)
        elif locality:
            description = _("Current weather conditions for {locality}").format(
                locality=locality)
        elif datetime and isinstance(datetime, DateTimeRepr):
            description = _("Weather conditions for {datetime}").format(
                datetime=datetime_s)
        else:
            description = _("Current weather conditions")
        return "{0}: {1}".format(description, self.__generate_random_forecast())

    def __generate_search_weather_forecast_condition_response(self, condition, locality, datetime):
        if not condition:
            return self.__generate_search_weather_forecast_response(locality, datetime)

        answer = self.__generate_response_for_condition(condition)
        datetime_s = DateUtils.to_string(datetime) if isinstance(
            datetime, DateTimeRepr) else None

        if locality and datetime_s:
            sentence = _("{answer} {datetime} in {locality}").format(
                answer=answer, datetime=datetime_s, locality=locality)
        elif locality:
            sentence = _("{answer} in {locality}").format(
                answer=answer, locality=locality)
        elif datetime_s:
            sentence = _("{answer} {datetime}").format(
                answer=answer, datetime=datetime_s, locality=locality)
        else:
            sentence = answer
        return sentence

    def __generate_random_forecast(self):
        degrees = random.choice([12, 15, 18, 21, 23])
        conditions = random.choice([_("cloudy"), _("rainy"), _(
            "thunder storms"), _("windy"), _("clear sky"), _("light wind")])
        return _("{conditions}, {degrees} degrees celcius").format(conditions=conditions, degrees=degrees)

    def __generate_response_for_condition(self, condition):
        yesNo = random.choice([True, False])
        if "rain" in condition:
            return random.choice(self.phrases["rain"][yesNo])
        elif "sun" in condition:
            return random.choice(self.phrases["sun"][yesNo])
        elif "wind" in condition:
            return random.choice(self.phrases["wind"][yesNo])
        return _("Sorry, we couldn't find the weather conditions")
