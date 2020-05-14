from page_objects import LoginPage


def test_adminlogin_page(remote):
    LoginPage(remote).go_site()
    LoginPage(remote).login_button()
    LoginPage(remote).username()
    LoginPage(remote).password()
    LoginPage(remote).forgot_password()
    LoginPage(remote).page_text()
    LoginPage(remote).close()
