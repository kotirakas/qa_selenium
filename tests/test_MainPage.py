from page_objects import MainPage


def test_mainpage():
    assert MainPage().featured() == "Featured"
    MainPage().first_carusel()
    MainPage().logo_carusel()
    MainPage().page_carusel()
    MainPage().content()
    MainPage().close()
