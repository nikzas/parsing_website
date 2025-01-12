from playwright.sync_api import sync_playwright


def run(playwright):
    browser = playwright.chromium.launch(headless=True, args=["--no-sandbox"])
    page = browser.new_page()

    # Переход на нужный сайт
    page.goto('https://1wzjvm.top/casino/play/1play_1play_luckyjet?p=7q53')
    page.wait_for_load_state('load')

    # Ожидание iframe
    iframe_element = page.wait_for_selector('iframe[src*="1play.gamedev-tech.cc/lucky/onewin"]', timeout=10000)

    # Получение содержимого iframe
    iframe = iframe_element.content_frame()

    if iframe:
        # Ожидание кнопки и клик по ней
        iframe.wait_for_selector('#history-button', state='visible', timeout=10000)
        iframe.locator('#history-button').click()

        # Получение элемента для скриншота
        element = page.wait_for_selector('.CasinoOneWinGame_game_goAwv', timeout=10000)

        # Получение размеров элемента
        box = element.bounding_box()
        if box:
            # Обрезка области скриншота
            screenshot_path = 'cropped_screenshot.png'
            page.screenshot(path=screenshot_path, clip={
                'x': box['x'],
                'y': box['y'],
                'width': 950,
                'height': 220
            })
            print(f'Screenshot saved to {screenshot_path}')
        else:
            print('Element not found!')
    else:
        print('Iframe not found!')

    browser.close()


with sync_playwright() as playwright:
    run(playwright)