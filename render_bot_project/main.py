import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://httpbin.org/get') as response:
            print(await response.text())

if __name__ == '__main__':
    asyncio.run(main())
