from find_iframe import *
import asyncio
from datetime import datetime, timedelta
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError, Error


async def main(url):
    async with async_playwright() as p:
        browser_args = [
            '--no-sandbox',
            '--disable-gpu',
            '--disable-software-rasterizer',
            '--disable-extensions',
            '--disable-dev-shm-usage'
        ]

        browser = await p.chromium.launch(
            headless=True,
            args=browser_args,
            handle_sigint=False,
            handle_sigterm=False,
            handle_sighup=False
        )
        while True:
            context = await browser.new_context()
            page = await context.new_page()
            await context.clear_cookies()
            start_time = datetime.now()
            while (datetime.now() - start_time) < timedelta(seconds=1):
                try:
                    await navigate_to_page(page, url)
                    target_frame = await wait_for_iframe(page)
                    if target_frame:
                        content = await fetch_history_from_frame(target_frame)
                        current_time, filename = await time_date()
                        await record_text(current_time, filename, content)
                except (PlaywrightTimeoutError, Error, TimeoutError, Exception) as e:
                    print(f"An unexpected error occurred: {e}, URL: {url}")
                finally:
                    await browser.close()

if __name__ == "__main__":
    url = "https://1wvec.com/casino/play/1play_1play_luckyjet"
    asyncio.run(main(url))
