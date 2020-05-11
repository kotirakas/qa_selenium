from page_objects import MainPage


def test_mainpage(browser, tim):
    MainPage(browser, tim).go_site()
    assert MainPage(browser, tim).featured() == "Featured"
    MainPage(browser, tim).first_carusel()
    MainPage(browser, tim).logo_carusel()
    MainPage(browser, tim).page_carusel()
    MainPage(browser, tim).content()
    web = browser.get_log("browser")
    l = 0
    for l in web:
        print(l)
        l += 1
    assert l == 0
    MainPage(browser, tim).close()
