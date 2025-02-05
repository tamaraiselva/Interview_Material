import asyncio
import aiohttp

# List of URLs to scrape
urls = [
    'https://example.com',
    'https://example.org',
    'https://example.net'
]

async def fetch(url, session):
    async with session.get(url) as response:
        print(f"Fetching {url}")
        return await response.text()

async def scrape_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch(url, session)) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

# Main event loop
async def main():
    html_pages = await scrape_all(urls)
    for idx, html in enumerate(html_pages):
        print(f"\nHTML content from {urls[idx]}:\n{html[:200]}...")  # Print first 200 chars

# Run the event loop
asyncio.run(main())
