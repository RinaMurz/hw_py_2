import pytest
@pytest.fixture()
def setting_browser():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    yield
    browser.quit()