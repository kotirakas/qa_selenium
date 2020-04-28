from page_objects import ProductPage


def test_product_page():
    ProductPage().description()
    ProductPage().add()
    ProductPage().quantity()
    ProductPage().review()
    ProductPage().price()
    ProductPage().close()
