from page_objects import CatalogPage
import logging
import argparse

def test_catalog_page(browser, tim):
    CatalogPage(browser, tim).go_site()
    CatalogPage(browser, tim).button()
    CatalogPage(browser, tim).sort()
    CatalogPage(browser, tim).limit()
    CatalogPage(browser, tim).compare()
    CatalogPage(browser, tim).content_name()
    #browser.save_screenshot('finish_test.png')
    web = browser.get_log("browser")
    l = 0
    for l in web:
        print(l)
        l += 1
    assert l == 0
    CatalogPage(browser, tim).close()
