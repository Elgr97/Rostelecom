from urllib.parse import urlparse
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.base_url = "https://b2c.passport.rt.ru"
        self.driver.implicitly_wait(timeout)

    def go_to_site(self):
        self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        try:
            return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                          message=f'Cannot find element: {locator}')
        except TimeoutException:
            print(f'TimeoutException: Cannot find element: {locator}')

    def find_many_elements(self, locator, time=10):
        try:
            return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                          message=f'Cannot find elements: {locator}')
        except TimeoutException:
            print(f'TimeoutException: Cannot find elements: {locator}')

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def find_element_until_to_be_clickable(self, locator, time=10):
        try:
            return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                          message=f'Element not clickable: {locator}')
        except TimeoutException:
            print(f'TimeoutException: Element not clickable: {locator}')
