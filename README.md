# aiotelegraf

[![Build Status](https://github.com/Gr1N/aiotelegraf/workflows/default/badge.svg)](https://github.com/Gr1N/aiotelegraf/actions?query=workflow%3Adefault) [![codecov](https://codecov.io/gh/Gr1N/aiotelegraf/branch/master/graph/badge.svg)](https://codecov.io/gh/Gr1N/aiotelegraf) ![PyPI](https://img.shields.io/pypi/v/aiotelegraf.svg?label=pypi%20version) ![PyPI - Downloads](https://img.shields.io/pypi/dm/aiotelegraf.svg?label=pypi%20downloads) ![GitHub](https://img.shields.io/github/license/Gr1N/aiotelegraf.svg)

An asyncio-base client for sending metrics to [Telegraf](https://www.influxdata.com/time-series-platform/telegraf/).

Implementation based on [pytelegraf](https://github.com/paksu/pytelegraf) package.

## Installation

```shell
$ pip install aiotelegraf
```

## Usage

```python
import asyncio
import aiotelegraf


async def main():
    client = aiotelegraf.Client(
        host='0.0.0.0',
        port=8089,
        tags={
            'my_global_tag_1': 'value_1',
            'my_global_tag_2': 'value_2',
        }
    )
    await client.connect()

    client.metric('my_metric_1', 'value_1', tags={
        'my_tag_1': 'value_1',
    })
    await client.close()


asyncio.run(main())
```

## Contributing

To work on the `aiotelegraf` codebase, you'll want to clone the project locally and install the required dependencies via [poetry](https://python-poetry.org):

```sh
$ git clone git@github.com:Gr1N/aiotelegraf.git
$ make install
```

To run tests and linters use command below:

```sh
$ make lint && make test
```

If you want to run only tests or linters you can explicitly specify which test environment you want to run, e.g.:

```sh
$ make lint-black
```

## License

`aiotelegraf` is licensed under the MIT license. See the license file for details.
