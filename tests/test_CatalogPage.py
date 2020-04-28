from page_objects import CatalogPage


def test_catalog_page():
    CatalogPage().button()
    CatalogPage().sort()
    CatalogPage().limit()
    CatalogPage().compare()
    CatalogPage().content_name()
    CatalogPage().close()
