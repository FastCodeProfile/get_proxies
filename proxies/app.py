import asyncio
import json

import aiohttp
from loguru import logger


class Proxies:
    def __init__(self) -> None:
        self.host = 'https://proxylist.geonode.com/api/proxy-list'
        self.params = {"limit": 500,
                       "page": 1,
                       "sort_by": "lastChecked",
                       "sort_type": "desc",
                       "speed": "fast"}

    async def get_http(self) -> dict:
        self.params["protocols"] = "http"
        async with aiohttp.ClientSession() as session:
            async with session.get(self.host, params=self.params) as response:
                json_response = await response.json()
                return json_response

    async def get_https(self) -> dict:
        self.params["protocols"] = "https"
        async with aiohttp.ClientSession() as session:
            async with session.get(self.host, params=self.params) as response:
                json_response = await response.json()
                return json_response

    async def get_socks4(self) -> dict:
        self.params["protocols"] = "socks4"
        async with aiohttp.ClientSession() as session:
            async with session.get(self.host, params=self.params) as response:
                json_response = await response.json()
                return json_response

    async def get_socks5(self) -> dict:
        self.params["protocols"] = "socks5"
        async with aiohttp.ClientSession() as session:
            async with session.get(self.host, params=self.params) as response:
                json_response = await response.json()
                return json_response


def dump_data(filename: str, data: dict) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)


async def main():
    proxies = Proxies()
    http = await proxies.get_http()
    dump_data('http.json', http)
    logger.success(f'Http-Прокси получены: {http["total"]}')
    https = await proxies.get_https()
    dump_data('https.json', https)
    logger.success(f'Https-Прокси получены: {https["total"]}')
    socks4 = await proxies.get_socks4()
    dump_data('socks4.json', socks4)
    logger.success(f'Socks4-Прокси получены: {socks4["total"]}')
    socks5 = await proxies.get_socks5()
    dump_data('socks5.json', socks5)
    logger.success(f'Socks5-Прокси получены: {socks5["total"]}')


if __name__ == '__main__':
    asyncio.run(main())
