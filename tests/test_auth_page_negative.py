import ast
import pickle
import time
import pytest
from pages.auth import *
from pages.settings import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.auth
@pytest.mark.negative
@pytest.mark.parametrize('username', [fake_phone, fake_login, invalid_ls],
                         ids=['fake phone', 'fake login', 'fake service account'])
def test_auth_page_fake_phone_login_serv_account(browser, username):
    """ Проверка авторизации по номеру телефона и паролю, лицевому счету,
    неверный номер/логин/лицевой счет."""
    page = AuthPage(browser)
    page.enter_username(username)
    page.enter_password(valid_password)
    page.btn_click_enter()
    browser.implicitly_wait(10)

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    forgot_pass = browser.find_element(*AuthLocators.AUTH_FORGOT_PASSWORD)

    assert error_mess.text == 'Неверный логин или пароль' and \
           page.check_color(forgot_pass) == '#ff4f12'


@pytest.mark.auth
@pytest.mark.negative
def test_auth_page_fake_email(browser):
    """Проверка авторизации по почте и паролю, неверная почта"""
    page = AuthPage(browser)
    page.enter_username(fake_email)
    page.enter_password(valid_pass_reg)
    
    # Ожидание появления капчи с таймаутом 30 секунд
    captcha = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'selector-for-captcha-element'))
    )

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    forgot_pass = browser.find_element(*AuthLocators.AUTH_FORGOT_PASSWORD)

    assert error_mess.text == 'Неверный логин или пароль' and \
           page.check_color(forgot_pass) == '#ff4f12'


@pytest.mark.auth
@pytest.mark.negative
@pytest.mark.parametrize('username', [valid_phone, valid_email, valid_login],
                         ids=['valid phone', 'valid login', 'valid email'])
def test_auth_page_fake_password(browser, username):
    """Проверка авторизации по номеру телефона/почте/логину и паролю. Неверный пароль.
    Тест по ЛС и паролю не проводился из-за отсутствия реальных тестовых данных"""
    page = AuthPage(browser)
    page.enter_username(username)
    page.enter_password(fake_password)
    page.btn_click_enter()
    browser.implicitly_wait(20)

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    forgot_pass = browser.find_element(*AuthLocators.AUTH_FORGOT_PASSWORD)

    assert error_mess.text == 'Неверный логин или пароль' and \
           page.check_color(forgot_pass) == '#ff4f12'


@pytest.mark.auth
@pytest.mark.negative
def test_auth_page_phone_empty_username(browser):
    """Проверка авторизации по телефону, пустой номер"""
    page = AuthPage(browser)
    page.clear_username_field()
    page.enter_password(valid_pass_phone)
    page.btn_click_enter()
    browser.implicitly_wait(10)

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)

    assert 'Поле обязательно для заполнения' in error_mess.text


@pytest.mark.auth
@pytest.mark.negative
@pytest.mark.parametrize('username', [1, 111111111],
                         ids=['one digit', '9 digits'])
def test_auth_page_invalid_username(browser, username):
    """Проверка авторизации по номеру телефона и паролю, неверный формат телефона"""
    page = AuthPage(browser)
    page.enter_username(username)
    page.enter_password(valid_password)
    page.btn_click_enter()
    browser.implicitly_wait(10)

    error_mess = browser.find_element(*AuthLocators.AUTH_MESS_ERROR)
    assert error_mess.text == 'Неверный формат телефона'
