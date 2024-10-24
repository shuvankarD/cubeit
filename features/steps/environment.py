# environment.py
from playwright.sync_api import sync_playwright

def before_scenario(context, scenario):
    # Start Playwright and open a browser instance before each scenario
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)  # You can set headless=True if you want to run headless
    context.page = context.browser.new_page()

def after_scenario(context, scenario):
    # Close the browser after each scenario
    context.page.close()
    context.browser.close()
    context.playwright.stop()