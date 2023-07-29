import os
import ast
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.first_name = driver.find_element(*RegLocators.REG_FIRSTNAME)
        self.last_name = driver.find_element(*RegLocators.REG_LASTNAME)
        self.email = driver.find_element(*RegLocators.REG_ADDRESS)
        self.password = driver.find_element(*RegLocators.REG_PASSWORD)
        self.pass_conf = driver.find_element(*RegLocators.REG_PASS_CONFIRM)
        self.btn = driver.find_element(*RegLocators.REG_REGISTER)

    def enter_firstname(self, value):
        self.first_name.send_keys(value)

    def enter_lastname(self, value):
        self.last_name.send_keys(value)

    def enter_email(self, value):
        self.email.send_keys(value)

    def enter_password(self, value):
        self.password.send_keys(value)

    def enter_pass_conf(self, value):
        self.pass_conf.send_keys(value)

    def click_button(self):
        self.btn.click()


class AuthPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv('MAIN_URL') or 'https://b2c.passport.rt.ru'
        driver.get(url)
        self.username = driver.find_element(*AuthLocators.AUTH_USERNAME)
        self.password = driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
        self.reg_in = driver.find_element(*AuthLocators.AUTH_REG_IN)
        self.active_tab = driver.find_element(*AuthLocators.AUTH_ACTIVE_TAB)

    def enter_username(self, value):
        self.username.send_keys(value)

    def enter_password(self, value):
        self.password.send_keys(value)

    def click_enter_button(self):
        self.btn.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, <locator of the expected element>))) #заменить <locator of the expected element> на локатор элемента, появление которого ожидается

    def enter_reg_page(self):
        self.reg_in.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, <locator of the expected element>))) #заменить <locator of the expected element> на локатор элемента, появление которого ожидается 
    
    def check_color(self, elem):
        try:
            rgba = elem.value_of_css_property('color')
            r, g, b, alpha = ast.literal_eval(rgba.strip('rgba'))
            return '#%02x%02x%02x' % (r, g, b)
        except Exception as e:
            print(f"Произошла ошибка при проверке цвета: {e}")
            return None

class NewPassPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials'
        driver.get(url)
        self.username = driver.find_element(*NewPassLocators.NEWPASS_ADDRESS)
        self.btn = driver.find_element(*NewPassLocators.NEWPASS_BTN_CONTINUE)

    def enter_username(self, value):
        self.username.send_keys(value)

    def click_continue_button(self):
        try:
            self.btn.click()
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located((By.XPATH, <locator of the expected element>))) #заменить <locator of the expected element> на локатор элемента, появление которого ожидается
        except Exception as e:
            print(f"Произошла ошибка при нажатии кнопки 'Продолжить': {e}")
