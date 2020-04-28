from page_objects import LoginPage


def test_adminlogin_page(browser,tim):
    LoginPage(browser, tim).go_site()
    LoginPage(browser, tim).login_button()
    LoginPage(browser, tim).username()
    LoginPage(browser, tim).password()
    LoginPage(browser, tim).forgot_password()
    LoginPage(browser, tim).page_text()
    LoginPage(browser, tim).close()