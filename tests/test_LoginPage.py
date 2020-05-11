from page_objects import LoginPage


def test_adminlogin_page(browser, tim):
    LoginPage(browser, tim).go_site()
    LoginPage(browser, tim).login_button()
    LoginPage(browser, tim).username()
    LoginPage(browser, tim).password()
    LoginPage(browser, tim).forgot_password()
    LoginPage(browser, tim).page_text()
    web = browser.get_log("browser")
    l = 0
    for l in web:
        print(l)
        l += 1
    assert l == 0
    LoginPage(browser, tim).close()
