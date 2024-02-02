
import asyncio
import aiohttp
import time

async def get_data_async(url, session):
    async with session.get(url) as response:
        return await response.json()

async def download_image(url, session, image_id):
    async with session.get(url) as response:
        with open(f"image_{image_id}.jpg", 'wb') as file:
            file.write(await response.read())

async def save_image():
    async with aiohttp.ClientSession() as session:
        tasks = [get_data_async(f"https://jsonplaceholder.typicode.com/photos/{i}", session) for i in range(1,101)]
        results = await asyncio.gather(*tasks)
        for result in results:
            await download_image(result['url'], session, result['id'])

if __name__ == '__main__':
    start = time.time()
    asyncio.run(save_image())
    end = time.time()
    print(end-start)