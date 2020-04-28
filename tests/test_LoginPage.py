from page_objects import LoginPage


def test_adminlogin_page():
    LoginPage().login_button()
    LoginPage().username()
    LoginPage().password()
    LoginPage().forgot_password()
    LoginPage().page_text()
    LoginPage().close()
