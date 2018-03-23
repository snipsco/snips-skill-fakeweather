# Fake Weather Forecasts skill for Snips

[![Build Status](https://travis-ci.org/snipsco/snips-skill-fakeweather.svg)](https://travis-ci.org/snipsco/snips-skill-fakeweather)
[![PyPi](https://img.shields.io/pypi/v/fakeweather.svg)](https://pypi.python.org/pypi/fakeweather)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/snipsco/snips-skill-fakeweather/master/LICENSE.txt)

We got fake news. Now let's get fake weather forecasts. This skill generates phrases with random weather forecasts for a given time and location, and is mainly for demo purposes.

## Usage

### Snips Skills Manager

It is recommended that you use this skill with the [Snips Skills Manager](https://github.com/snipsco/snipsskills). Simply add the following section to your [Snipsfile](https://github.com/snipsco/snipsskills/wiki/The-Snipsfile):

```yaml
skills:
  - pip: snipsfakeweather
    package_name: snipsfakeweather
    class_name: SnipsFakeWeather
    requires_tts: True
```


### Standalone

If you do not wish to use the skill via the Snips Manager, the skill is on [PyPI](https://pypi.python.org/pypi/snipsfakeweather), so you can just install it with [pip](http://www.pip-installer.org):

```sh
$ pip install snipsfakeweather
```

You may now import it into your Python project:

```python

from snipsfakeweather.snipsfakeweather import SnipsFakeWeather

weather = SnipsFakeWeather() 
weather.speak_forecast("Paris,fr")
```

## Contributing

Please see the [Contribution Guidelines](https://github.com/snipsco/snips-skill-fakeweather/blob/master/CONTRIBUTING.md).

## Copyright

This skill is provided by [Snips](https://www.snips.ai) as Open Source software. See [LICENSE.txt](https://github.com/snipsco/snips-skill-fakeweather/blob/master/LICENSE.txt) for more information.
