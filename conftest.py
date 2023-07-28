import time
import pytest
from selenium import webdriver
from faker import Faker


@pytest.fixture(autouse=True)
def browser():
   driver = webdriver.Firefox(executable_path='firefox.exe')

    yield driver
    driver.quit()
