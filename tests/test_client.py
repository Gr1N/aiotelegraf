import asyncio

import pytest

import aiotelegraf


@pytest.fixture
def cfg():
    return {
        'host': '0.0.0.0',
        'port': 8089,
    }


@pytest.fixture
async def client(cfg):
    client = aiotelegraf.Client(**cfg)

    await client.connect()
    yield client
    await client.close()


@pytest.fixture
def udpserver(event_loop, cfg):
    datagrams = []

    class Protocol(asyncio.DatagramProtocol):
        def datagram_received(self, data, _addr):
            datagrams.append(data.decode())

    class Server:
        def __init__(self):
            self._transport = None

        async def __aenter__(self):
            listen = event_loop.create_datagram_endpoint(
                Protocol,
                local_addr=(
                    cfg['host'],
                    cfg['port'],
                )
            )
            self._transport, _ = await listen

        async def __aexit__(self, _exc_type, _exc, _tb):
            self._transport.close()
            self._transport = None

    yield Server(), datagrams


async def wait_for_result(datagrams, *, expected_count=1):
    attempts = 0
    while True:
        if len(datagrams) == expected_count:
            break
        elif attempts < 10:
            attempts += 1
            await asyncio.sleep(0.5)
        else:
            raise RuntimeError('Failed to receive datagrams')


@pytest.mark.asyncio
async def test_client__ok(client, udpserver):
    server, datagrams = udpserver

    async with server:
        client.metric('test_name_1', 'test_value_1')
        client.metric('test_name_2', 'test_value_2')

        await wait_for_result(datagrams, expected_count=2)

    message = datagrams[0]
    assert message == 'test_name_1 value="test_value_1"\n'

    message = datagrams[1]
    assert message == 'test_name_2 value="test_value_2"\n'
