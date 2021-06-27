import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru', help='Chose language')

@pytest.fixture(scope="function")
def browser(request):

	# считываем язык и браузер (если есть)
	choosen_language = request.config.getoption("language")
    # инициализируем браузер chrome с нужными опциями
	opts = Options()
	opts.add_experimental_option('prefs', {'intl.accept_languages': choosen_language})
	print('\nstart Chrome browser...')
	browser = webdriver.Chrome(options=opts)
	yield browser
	# закрытие браузера после работы
	browser.quit()