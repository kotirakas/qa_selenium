from selenium import webdriver


def test_browsers(browser, url_base):
    if browser == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        wd = webdriver.Chrome(options=options)
    elif browser == "Firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")
        wd = webdriver.Firefox(options=options)
    elif browser == "Edge":
        wd = webdriver.Edge()
    wd.get(url_base)
    title_page = wd.title
    assert title_page == "Your Store"
    wd.close()
