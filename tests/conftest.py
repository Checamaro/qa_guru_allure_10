import pytest
from selene import browser

@pytest.fixture(scope='session', autouse=True)
def browser_management():
    browser.config.base_url = 'https://github.com';
    browser.config.window_width = 1500
    browser.config.window_height = 900
    yield
    browser.quit()