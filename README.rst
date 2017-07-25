Fake weather forecasts skill for Snips
======================================

|Build Status| |PyPI| |MIT License|

We got fake news. Now let's get fake weather forecasts.

Installation
------------

The skill is on `PyPI`_, so you can just install it with `pip`_:

.. code-block:: console

    $ pip install snipsfakeweather

Usage
-----

The skill presents fake weather forecasts for demo purposes.

.. code-block:: python

    from snipsfakeweather.snipsfakeweather import SnipsFakeWeather

    weather = SnipsFakeWeather() 
    weather.speak_forecast("Paris,fr")

Copyright
---------

This skill is provided by `Snips`_ as Open Source software. See `LICENSE.txt`_ for more
information.

.. |Build Status| image:: https://travis-ci.org/snipsco/snips-skill-fakeweather.svg
   :target: https://travis-ci.org/snipsco/snips-skill-fakeweather
   :alt: Build Status
.. |PyPI| image:: https://img.shields.io/pypi/v/snipsfakeweather.svg
   :target: https://pypi.python.org/pypi/snipsfakeweather
   :alt: PyPI
.. |MIT License| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://raw.githubusercontent.com/snipsco/snips-skill-hue/master/LICENSE.txt
   :alt: MIT License

.. _`PyPI`: https://pypi.python.org/pypi/snipsfakeweather
.. _`pip`: http://www.pip-installer.org
.. _`Snips`: https://www.snips.ai
.. _`OpenWeatherMap website`: https://openweathermap.org/api
.. _`LICENSE.txt`: https://github.com/snipsco/snips-skill-hue/blob/master/LICENSE.txt
