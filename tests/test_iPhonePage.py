from page_objects import iPhonePage


def test_add_cart(remote):
    iPhonePage(remote).go_site()
    assert iPhonePage(remote).add_to_cart() == iPhonePage(remote).CART_NAME
    iPhonePage(remote).close()


def test_device_name(remote):
    iPhonePage(remote).go_site()
    assert iPhonePage(remote).device_name() == iPhonePage(remote).NAME
    iPhonePage(remote).close()


def test_brand_name(remote):
    iPhonePage(remote).go_site()
    assert iPhonePage(remote).brand_name() == iPhonePage(remote).BRAND
    iPhonePage(remote).close()


def test_product_code(remote):
    iPhonePage(remote).go_site()
    assert iPhonePage(remote).product_code() == iPhonePage(remote).CODE
    iPhonePage(remote).close()


def test_availability(remote):
    iPhonePage(remote).go_site()
    assert iPhonePage(remote).availability_status() == iPhonePage(remote).STATUS
    iPhonePage(remote).close()
