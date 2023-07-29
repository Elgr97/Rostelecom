import pytest
from pages.auth import AuthPage
from selenium.webdriver.common.by import By
from pages.settings import valid_phone, valid_login, valid_password, invalid_ls, valid_email, valid_pass_reg

@pytest.fixture
def auth_page(browser):
    return AuthPage(browser)

@pytest.mark.parametrize('username', ['valid_phone', 'valid_email', 'valid_login', 'invalid_ls'],
                         ids=['phone', 'email', 'login', 'ls'])
def test_active_tab(auth_page, username):
    """Проверка автоматического переключения табов телефон/email/логин/лицевой счет"""
    
    auth_page.enter_username(username)
    auth_page.enter_password('valid_password')
    
    if username == 'valid_phone':
        active_tab_element = auth_page.get_active_tab()
        assert active_tab_element == 'Телефон'
    elif username == 'valid_email':
        active_tab_element = auth_page.get_active_tab()
        assert active_tab_element == 'Почта'
    elif username == 'valid_login':
        active_tab_element == auth_page.get_active_tab()
        assert active_tab_element == 'Логин'
    else:
        active_tab_element = auth_page.get_active_tab()
        assert active_tab_element == 'Лицевой счет'


def test_invalid_password(auth_page):
    """Проверка авторизации с недопустимым паролем"""
    
    auth_page.enter_username('valid_username')
    auth_page.enter_password('invalid_password')
    auth_page.submit_form()

    assert auth_page.get_error_message() == "Invalid password"
	
	
@pytest.mark.parametrize('username', ['valid_phone', 'valid_login'],
                         ids=['valid phone', 'valid login'])
def test_auth_page_phone_login_valid(auth_page, username):
    """Проверка авторизации по номеру телефона/логину и паролю + проверка
    автоматического переключения табов тел/логин (для проверки нужен зарегистрированный номер телефона)"""
    
    auth_page.enter_username(username)
    auth_page.enter_password('valid_password')
    auth_page.btn_click_enter()

    assert auth_page.get_relative_link() == '/account_b2c/page'


@pytest.mark.screenshot
def test_auth_page_email_valid(auth_page):
    """Проверка авторизации по почте и паролю"""
    
    auth_page.enter_username('valid_email')
    auth_page.enter_password('valid_pass_reg')
    auth_page.submit_form()
    
    assert auth_page.get_relative_link() == '/account_b2c/page'


def test_captcha(auth_page, monkeypatch):
    """Проверка авторизации с Captcha"""
    
    auth_page.enter_username('valid_email')
    auth_page.enter_password('valid_password')
    
    def mock_is_captcha_present():
        return True
    
    monkeypatch.setattr(auth_page, 'is_captcha_present', mock_is_captcha_present)
    
    # Вводим данные для капчи
    captcha_code = 'captcha_code'
    auth_page.enter_captcha(captcha_code)
    auth_page.submit_form()
    
    assert auth_page.is_logged_in()

def test_no_captcha(auth_page, monkeypatch):
    """Проверка авторизации без Captcha"""
    
    auth_page.enter_username('valid_email')
    auth_page.enter_password('valid_password')
    
    def mock_is_captcha_present():
        return False
    
    monkeypatch.setattr(auth_page, 'is_captcha_present', mock_is_captcha_present)
    
    auth_page.submit_form()
    
    assert auth_page.is_logged_in()
