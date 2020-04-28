from selenium import webdriver


class LoginPage:
    LOGIN_BUTTON = "button[type=submit]"
    USERNAME = "input#input-username"
    PASSWORD = "input#input-password"
    FORGOT_PASSWORD = "Forgotten Password"
    PAGE_TEXT = "h1"
    browser = webdriver.Chrome()
    browser.get("https://demo.opencart.com/admin/")

    def login_button(self):
        self.browser.find_element_by_css_selector(self.LOGIN_BUTTON)  # кнопка логин

    def username(self):
        self.browser.find_element_by_css_selector(self.USERNAME)  # поле ввода логина

    def password(self):
        self.browser.find_element_by_css_selector(self.PASSWORD)  # поле ввода пвроля

    def forgot_password(self):
        self.browser.find_element_by_link_text(self.FORGOT_PASSWORD)  # ссылка "забыл пароль#

    def page_text(self):
        self.browser.find_element_by_tag_name(self.PAGE_TEXT)

    def close(self):
        self.browser.close()
