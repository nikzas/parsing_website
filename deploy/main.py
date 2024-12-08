from func_mode import fetch_data, time_date, record_text
import asyncio
from playwright.async_api import async_playwright
from datetime import datetime, timedelta

async def main():
    async with async_playwright() as p:
        while True:
            browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
            context = await browser.new_context()
            page = await context.new_page()
            await context.clear_cookies()

            start_time = datetime.now()
            while (datetime.now() - start_time) < timedelta(seconds=3):
                text_content = await fetch_data(page)
                current_time, filename = await time_date()
                await record_text(current_time, filename, text_content)
            await browser.close()
            await asyncio.sleep(7)

asyncio.run(main())
