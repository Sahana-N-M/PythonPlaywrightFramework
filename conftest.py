import pytest
import allure
from playwright.sync_api import sync_playwright
from utils.config_reader import ConfigReader


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser_name = ConfigReader.get_browser()
        headless = ConfigReader.is_headless()
        slow_mo = ConfigReader.get_slow_mo()

        browser = getattr(p, browser_name).launch(headless=headless, slow_mo=slow_mo)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser, request):
    context = browser.new_context()
    page = context.new_page()

    page.goto(ConfigReader.get_base_url(), wait_until="domcontentloaded")

    yield page

    # Always take screenshot after test execution (Passed/Failed)
    screenshot = page.screenshot(full_page=True)

    allure.attach(
        screenshot,
        name=f"{request.node.name}_screenshot",
        attachment_type=allure.attachment_type.PNG
    )

    context.close()


# Hook to get test status (Passed/Failed)
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)