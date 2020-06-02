""" bbb"""
from page_objects import MainPage


def test_mainpage(remote):
    """ aaa"""
    MainPage(remote).go_site()
    assert MainPage(remote).featured() == "Featured"
    MainPage(remote).first_carusel()
    MainPage(remote).logo_carusel()
    MainPage(remote).page_carusel()
    MainPage(remote).content()
    MainPage(remote).close()
