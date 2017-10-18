Fake Weather Forecasts skill for Snips
======================================

|Build Status| |PyPI| |MIT License|

We got fake news. Now let's get fake weather forecasts. This skill generates phrases with random weather forecasts for a given time and location, and is mainly for demo purposes.

Usage
-----

Snips Skills Manager
^^^^^^^^^^^^^^^^^^^^

It is recommended that you use this skill with the `Snips Skills Manager <https://github.com/snipsco/snipsskills>`_. Simply add the following section to your `Snipsfile <https://github.com/snipsco/snipsskills/wiki/The-Snipsfile>`_:

.. code-block:: yaml

  skills:
  - package_name: snipsfakeweather
    class_name: SnipsFakeWeather
    pip: snipsfakeweather
    requires_tts: True

Standalone usage
^^^^^^^^^^^^^^^^

If you do not wish to use the Snips Skills Manager, it can be used as a standalone Python module. It is on `PyPI`_, so you can just install it with `pip`_:

.. code-block:: console

    $ pip install snipsfakeweather

You may now import it into your Python project:

.. code-block:: python

    from snipsfakeweather.snipsfakeweather import SnipsFakeWeather

    weather = SnipsFakeWeather() 
    weather.speak_forecast("Paris,fr")

Contributing
------------

Please see the `Contribution Guidelines`_.

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
.. _`Contribution Guidelines`: https://github.com/snipsco/snips-skill-hue/blob/master/CONTRIBUTING.rst
.. _snipsskills: https://github.com/snipsco/snipsskills
