from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError, Error
import asyncio
from datetime import datetime
import aiofiles

async def navigate_to_page(page, url):
    await page.goto(url)

async def wait_for_iframe(page, timeout=10000):
    await page.wait_for_selector("iframe", timeout=timeout)
    frames = page.frames

    for frame in frames:
        if "https://1play.gamedev-tech.cc/" in frame.url:
            return frame
    return None

async def fetch_history_from_frame(frame):
    await frame.wait_for_selector('#history', timeout=10000)
    history_container = await frame.query_selector('#history')

    if history_container:
        number_elements = await history_container.query_selector_all('div[id^="history-item-"]')
        all_texts = []

        for element in number_elements:
            try:
                text_content = await element.text_content() if element else "No content"
                all_texts.append(text_content)  # Добавляем текст в список
            except (PlaywrightTimeoutError, Error, TimeoutError) as e:
                print(f"Error getting text: {e}")

        return all_texts
    else:
        print("History container not found.")
        return ""

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