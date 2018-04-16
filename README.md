# aiotelegraf [![Build Status](https://travis-ci.org/Gr1N/aiotelegraf.svg?branch=master)](https://travis-ci.org/Gr1N/aiotelegraf) [![codecov](https://codecov.io/gh/Gr1N/aiotelegraf/branch/master/graph/badge.svg)](https://codecov.io/gh/Gr1N/aiotelegraf)

An asyncio-base client for sending metrics to [Telegraf](https://www.influxdata.com/time-series-platform/telegraf/).

Implementation based on [pytelegraf](https://github.com/paksu/pytelegraf) package.

## Installation

    $ pip install aiotelegraf

## Usage

    import asyncio
    import aiotelegraf

    loop = asyncio.get_event_loop()
    r = loop.run_until_complete

    client = aiotelegraf.Client(
        host='0.0.0.0',
        port=8089,
        tags={
            'my_global_tag_1': 'value_1',
            'my_global_tag_2': 'value_2',
        }
    )
    r(client.connect())

    client.metric('my_metric_1', 'value_1', tags={
        'my_tag_1': 'value_1',
    })
    r(client.close())

## Testing and linting

For testing and linting install [tox](http://tox.readthedocs.io):

    $ pip install tox

...and run:

    $ tox

## License

`aiotelegraf` is licensed under the MIT license. See the license file for details.
