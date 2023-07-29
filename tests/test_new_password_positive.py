import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.registration_email import RegistrationEmail
from pages.auth import AuthPage
from pages.settings import *
from pages.new_pass import NewPassPage
from pages.new_pass_locators import NewPassLocators

class TestNewPasswordPositive:
    @pytest.mark.newpass
    @pytest.mark.positive
    def test_forgot_password_page(self, browser):
	
		#Проверка восстановления пароля по почте.
        email_page = NewPassPage(browser)
        email_page.enter_username(valid_email)
        email_page.btn_click_continue()

        wait = WebDriverWait(browser, 25)
        wait.until(EC.presence_of_element_located((By.XPATH,
		'//*[@id="id_of_element"]')))

        #Проверяем почтовый ящик на наличие писем и достаём ID последнего письма
        mail_name, mail_domain = valid_email.split('@')

        id_letter, status_id = RegistrationEmail().get_id_letter(mail_name, mail_domain)
		
		#Сверяем полученные данные
        assert status_id == 200, "status_id error"
        assert id_letter > 0, "id_letter > 0 error"

        id_letter = str(id_letter[0]['id'])
		
        #Получаем код регистрации из письма от Ростелекома
        code, status_code = RegistrationEmail().get_reg_code(mail_name, mail_domain, id_letter)
        assert status_code == 200, "status_code error"
		
		#Получаем body из текста письма:
        text_body = code['body']
		
		#Извлекаем код из текста методом find:
        reg_code = text_body[text_body.find('Ваш код: ') + len('Ваш код: '):
                             text_body.find('Ваш код: ') + len('Ваш код: ') + 6]
							 
		#Сверяем полученные данные					 
        assert reg_code != '', "reg_code != [] error"

        digits = [int(char) for char in reg_code]
        print(digits)

        for i, digit in enumerate(reg_code):
            element = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="digit_{i+1}"]')))
            element.send_keys(digit)

        new_pass = fake_password
        browser.find_element(*NewPassLocators.NEWPASS_NEW_PASS).send_keys(new_pass)     browser.find_element(*NewPassLocators.NEWPASS_NEW_PASS_CONFIRM).send_keys(new_pass)
        browser.find_element(*NewPassLocators.NEWPASS_BTN_SAVE).click()

        #В случае успешной смены пароля, перезаписываем его в файл settings     wait.until(EC.url_matches('/auth/realms/b2c/login-actions/authenticate'))
        assert email_page.get_relative_link() == '/auth/realms/b2c/login-actions/authenticate'

        with open(r"../pages/settings.py", 'r', encoding='utf8') as file:
            lines = []
            for line in file.readlines():
                if 'valid_pass_reg' in line:
                    lines.append(f"valid_pass_reg = '{fake_password}'\n")
                else:
                    lines.append(line)
        with open(r"../pages/settings.py", 'w', encoding='utf8') as file:
            file.writelines(lines)
