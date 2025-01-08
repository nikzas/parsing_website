import asyncio
from playwright.async_api import async_playwright
from datetime import datetime
import aiofiles

async def fetch_data(page):
    try:
        await page.goto('https://1wzjvm.top/casino/play/1play_1play_luckyjet?p=7q53')
        await page.wait_for_load_state('load')
        await asyncio.sleep(8)  # Возможно, это можно убрать или уменьшить

        iframe = await get_iframe(page)
        if iframe:
            return await get_text_from_iframe(iframe, page)
        else:
            print("Iframe не найден")
            await take_screenshot(page)
            return "Iframe not found"
    except Exception as e:
        await take_screenshot(page)
        print(f"Failed to fetch data: {e}")
        return "Error fetching data"

async def get_iframe(page):
    await page.wait_for_selector('iframe[src*="1play.gamedev-tech.cc/lucky/onewin"]', timeout=10000)
    return page.frame(url=lambda url: "1play.gamedev-tech.cc/lucky/onewin" in url)

async def get_text_from_iframe(iframe, page):
    await iframe.wait_for_selector('#history-button', state='visible', timeout=10000)
    await iframe.locator('#history-button').click()
    await iframe.wait_for_selector('.sc-gJCZQp', state='visible', timeout=10000)
    text = await iframe.locator('.sc-gJCZQp').inner_text()

    await take_screenshot(page)

    if len(text) >= 20:
        return text.split('\n')
    else:
        print("Полученный текст слишком короткий.")
        await take_screenshot_else(page)
        await page.reload()
        return await get_text_from_iframe(await get_iframe(page), page)

async def take_screenshot(page):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    await page.screenshot(path=f"screenshots/screenshots-{timestamp}.png")

async def take_screenshot_else(page):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    await page.screenshot(path=f"screenshots/screenshots-{timestamp}-ELSE.png")

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

async def process_data(page):
    # Получаем данные с веб-страницы
    text_content = await fetch_data(page)

    # Получаем текущее время и имя файла для записи
    current_time, filename = await time_date()

    # Записываем полученные данные в файл
    await record_text(current_time, filename, text_content)