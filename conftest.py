import pytest
import importlib.util
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        '--language',
        action='store',
        default='ru, en',  # или default=None,
        help='Language'
    )


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    print('\nStart default browser Chrome for test..')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    driver = webdriver.Chrome(options=options)

    yield driver

    print('\nQuit browser..')
    driver.quit()
