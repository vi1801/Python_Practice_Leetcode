import asyncio
import aiohttp


async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.json()


async  def fetch_all_data(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        result = await asyncio.gather(*tasks)
        return result


# entry point
def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3",
    ]
    result = asyncio.run(fetch_all_data(urls))
    for i, result in enumerate(result, 1):
        print(f"API {i} response: {result}")


if __name__ == "__main__":
    main()