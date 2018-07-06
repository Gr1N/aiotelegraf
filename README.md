# aiotelegraf [![Build Status](https://travis-ci.org/Gr1N/aiotelegraf.svg?branch=master)](https://travis-ci.org/Gr1N/aiotelegraf) [![codecov](https://codecov.io/gh/Gr1N/aiotelegraf/branch/master/graph/badge.svg)](https://codecov.io/gh/Gr1N/aiotelegraf) [![Updates](https://pyup.io/repos/github/Gr1N/aiotelegraf/shield.svg)](https://pyup.io/repos/github/Gr1N/aiotelegraf/) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

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

## Contributing

To work on the `aiotelegraf` codebase, you'll want to clone the project locally and install the required dependencies via [poetry](https://poetry.eustace.io):

    $ git clone git@github.com:Gr1N/aiotelegraf.git
    $ poetry install

To run tests and linters use command below:

    $ poetry run tox

If you want to run only tests or linters you can explicitly specify which test environment you want to run, e.g.:

    $ poetry run tox -e py36-tests

## License

`aiotelegraf` is licensed under the MIT license. See the license file for details.
