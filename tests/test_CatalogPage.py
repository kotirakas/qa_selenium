from page_objects import CatalogPage


def test_catalog_page(browser, tim):
    CatalogPage(browser, tim).go_site()
    CatalogPage(browser, tim).button()
    CatalogPage(browser, tim).sort()
    CatalogPage(browser, tim).limit()
    CatalogPage(browser, tim).compare()
    CatalogPage(browser, tim).content_name()
    CatalogPage(browser, tim).close()
