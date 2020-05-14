from page_objects import CatalogPage


def test_catalog_page(remote):
    CatalogPage(remote).go_site()
    CatalogPage(remote).button()
    CatalogPage(remote).sort()
    CatalogPage(remote).limit()
    CatalogPage(remote).compare()
    CatalogPage(remote).content_name()
    CatalogPage(remote).close()
