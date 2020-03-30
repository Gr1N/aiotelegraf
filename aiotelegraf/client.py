import asyncio
from asyncio.transports import DatagramTransport
from typing import Any, Optional

from telegraf.client import ClientBase

from aiotelegraf import compat

__all__ = ("Client",)


class Client(ClientBase):
    __slots__ = ("_protocol",)

    def __init__(
        self, *, host: str = "localhost", port: int = 8094, tags: Optional[dict] = None
    ) -> None:
        super().__init__(host=host, port=port, tags=tags)

        self._protocol = DatagramProtocol()

    async def connect(self) -> None:
        loop = compat.get_event_loop()
        await loop.create_datagram_endpoint(
            lambda: self._protocol, remote_addr=(self.host, self.port)
        )

    async def close(self) -> None:
        self._protocol.close()

    def metric(
        self,
        measurement_name: str,
        values: Any,
        *,
        tags: Optional[dict] = None,
        timestamp: Optional[int] = None,
    ) -> None:
        super().metric(measurement_name, values, tags=tags, timestamp=timestamp)

    def send(self, data: str) -> None:
        self._protocol.send(data)


class DatagramProtocol(asyncio.DatagramProtocol):
    __slots__ = ("_transport",)

    def __init__(self) -> None:
        self._transport: Optional[DatagramTransport] = None

    def close(self) -> None:
        if self._transport is None:
            return

        self._transport.close()

    def connection_made(self, transport):
        self._transport = transport

    def connection_lost(self, _exc):
        self._transport = None

    def send(self, data: str) -> None:
        if self._transport is None:
            return

        try:
            self._transport.sendto(f"{data}\n".encode("utf-8"))
        except:  # noqa: E722
            # Errors should fail silently so they don't affect anything else
            pass
