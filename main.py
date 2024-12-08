from find_iframe import *
import asyncio
from datetime import datetime, timedelta

async def main(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        try:
            await navigate_to_page(page, url)
            target_frame = await wait_for_iframe(page)
            if target_frame:
                await fetch_history_from_frame(target_frame)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    url = "https://1wvec.com/casino/play/1play_1play_luckyjet"
    asyncio.run(main(url))
