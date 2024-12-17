import os
import yaml
import asyncio
import logging
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
from datetime import datetime

# ログディレクトリの設定
log_dir = os.path.join(os.path.dirname(__file__), '../logs')
os.makedirs(log_dir, exist_ok=True)

# ログファイル名の生成（YYYYMMDD.log）
log_filename = datetime.now().strftime('%Y%m%d') + '.log'
log_path = os.path.join(log_dir, log_filename)

# ログ設定の追加
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler()
    ]
)

# 同時実行タスクの制限
MAX_CONCURRENT_TASKS = 1  # 必要に応じて調整
semaphore = asyncio.Semaphore(MAX_CONCURRENT_TASKS)

async def load_config(config_path):
    with open(config_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

async def take_screenshot(page, test_name, count, width, height, output_path, test_settings, url, retries=3):
    for attempt in range(1, retries + 1):
        try:
            # ウィンドウサイズを変更
            await page.set_viewport_size({"width": width, "height": height})
            logging.info(f"[{test_name}] ビューポートサイズ変更: {width}x{height} [試行 {attempt}]")

            # レスポンシブデザインが適用されるように少し待機
            await asyncio.sleep(1)

            # ページ読み込み後の待機時間
            wait_time = test_settings.get('wait_time', 2000)  # デフォルトは2秒
            await asyncio.sleep(wait_time / 1000)  # ミリ秒を秒に変換

            # スクリーンショットを取得
            await page.screenshot(path=output_path, full_page=True)
            logging.info(f"[{test_name}] スクリーンショット保存: {output_path}")

            break  # 成功したらループを抜ける
        except (PlaywrightTimeoutError, Exception) as e:
            logging.error(f"[{test_name}] スクリーンショット取得失敗 ({width}x{height}) [試行 {attempt}]: {e}")
            if attempt < retries:
                await asyncio.sleep(2)  # 再試行前に待機
            else:
                logging.error(f"[{test_name}] 全ての試行が失敗しました: {url} - {width}x{height}")

async def process_test(playwright, test, browsers, timestamp):
    test_name = test.get('name')
    url = test.get('url')
    test_settings = test.get('settings', {})

    # ブラウザを1回だけ起動
    browser = await playwright.chromium.launch(headless=True)  # Chromeのみ使用

    # コンテキスト作成時にCookieを設定
    cookies = test_settings.get('cookies', [])
    if cookies:
        context = await browser.new_context()
        # Cookieを追加
        await context.add_cookies(cookies)
        logging.info(f"[{test_name}] 設定されたCookie: {cookies}")
    else:
        context = await browser.new_context()

    # 新しいページを作成
    page = await context.new_page()

    # 初回ページアクセス
    logging.info(f"[{test_name}] アクセス中: {url}")
    try:
        response = await page.goto(url, timeout=60000)  # タイムアウトを60秒に設定
    except PlaywrightTimeoutError:
        logging.error(f"[{test_name}] ページの読み込みにタイムアウトしました。")
        await page.close()
        await context.close()
        await browser.close()
        return

    if not response or not response.ok:
        logging.error(f"[{test_name}] ページの読み込みに失敗しました。ステータスコード: {response.status if response else 'N/A'}")
        await page.close()
        await context.close()
        await browser.close()
        return

    # ページ読み込み後の待機時間
    wait_time = test_settings.get('wait_time', 2000)  # デフォルトは2秒
    await asyncio.sleep(wait_time / 1000)  # ミリ秒を秒に変換

    # 各ブラウザサイズごとにスクリーンショットを取得
    for count, browser_conf in enumerate(browsers, 1):
        width = browser_conf.get('width')
        height = browser_conf.get('height')

        # スクリーンショットの保存先ディレクトリを作成
        output_dir = os.path.join(os.path.dirname(__file__), '../screenshots', test_name)
        os.makedirs(output_dir, exist_ok=True)

        # ファイル名にテスト名、回数、ブラウザサイズ、タイムスタンプを含める
        filename = f"{test_name}_{count}_chromium_{width}x{height}_{timestamp}.png"
        output_path = os.path.join(output_dir, filename)

        # スクリーンショット取得タスクを追加
        await take_screenshot(page, test_name, count, width, height, output_path, test_settings, url)

    # ページ、コンテキスト、ブラウザを閉じる
    await page.close()
    await context.close()
    await browser.close()

async def main():
    config_path = os.path.join(os.path.dirname(__file__), '../config/config.yaml')
    config = await load_config(config_path)

    browsers = config.get('browsers', [])
    tests = config.get('tests', [])

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    async with async_playwright() as playwright:
        tasks = []
        for test in tests:
            tasks.append(
                process_test(playwright, test, browsers, timestamp)
            )
        await asyncio.gather(*tasks)
        logging.info("全てのスクリーンショットを取得しました。")

if __name__ == "__main__":
    asyncio.run(main())
