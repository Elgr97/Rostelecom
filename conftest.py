import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture(scope='session')
def browser():
    """Инициализация браузера перед выполнением тестов"""
    # Настройки FirefoxDriver
    options = Options()
    options.add_argument('-headless')  # Запуск браузера в режиме "без головы"

    # Инициализация WebDriver
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()

    # Переход к странице авторизации
    driver.get('https://b2c.passport.rt.ru')

    yield driver

    # Завершение работы WebDriver после выполнения тестов
    driver.quit()
