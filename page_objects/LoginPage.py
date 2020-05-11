import logging

logger = logging.getLogger(__name__)


class LoginPage:
    def __init__(self, driver, tim):
        self.tim = tim
        self.driver = driver
        self.base_url = 'https://demo.opencart.com/admin/'

    def go_site(self):
        logger.info('====== Started LoginPage ======')
        return self.driver.get(self.base_url)

    LOGIN_BUTTON = "button[type=submit]"
    USERNAME = "input#input-username"
    PASSWORD = "input#input-password"
    FORGOT_PASSWORD = "Forgotten Password"
    PAGE_TEXT = "h1"

    def login_button(self):
        self.driver.find_element_by_css_selector(self.LOGIN_BUTTON)  # кнопка логин

    def username(self):
        self.driver.find_element_by_css_selector(self.USERNAME)  # поле ввода логина

    def password(self):
        self.driver.find_element_by_css_selector(self.PASSWORD)  # поле ввода пвроля

    def forgot_password(self):
        self.driver.find_element_by_link_text(self.FORGOT_PASSWORD)  # ссылка "забыл пароль#

    def page_text(self):
        self.driver.find_element_by_tag_name(self.PAGE_TEXT)

    def close(self):
        logger.info('====== Closed LoginPage ======')
        self.driver.close()
