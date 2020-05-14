from page_objects import ProductPage


def test_product_page(remote):
    ProductPage(remote).go_site()
    ProductPage(remote).description()
    ProductPage(remote).add()
    ProductPage(remote).quantity()
    ProductPage(remote).review()
    ProductPage(remote).price()
    ProductPage(remote).close()
