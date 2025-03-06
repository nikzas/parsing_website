import asyncio
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError, Error
from datetime import datetime
import aiofiles

async def fetch_data(page):
    try:
        await page.goto(
            "https://100hp.app/lucky/onewin/?exitUrl=https%253A%252F%252F1wwxqc.win%252Fcasino&language=ru&b=demo"
        ) 
        element = await page.wait_for_selector('.sc-gJCZQp', state="visible", timeout=10000)
        text_content = await element.text_content() if element else "No content"
        return text_content
    except (PlaywrightTimeoutError, Error, TimeoutError) as e:
        page.screenshot(path=f"{datetime.now()}.png")
        print(f"Failed to fetch data: {e}")
        return "Error fetching data"

async def time_date():
    current_datetime = datetime.now()
    current_date = current_datetime.strftime("%Y-%m-%d")
    current_time = current_datetime.strftime("%H:%M:%S")
    filename = f"{current_date}.txt"
    return current_time, filename

async def record_text(current_time, filename, text_content):
    try:
        async with aiofiles.open(filename, 'a', encoding='utf-8') as file:
            await file.write(f"{current_time} - {text_content}\n")
    except Exception as e:
        print(f"Failed to record text: {e}")


#"https://lucky-jet.gamedev-atech.cc/?exitUrl=https%253A%252F%252F1wowei.xyz%252Fcasino&language=ru&b=demo"