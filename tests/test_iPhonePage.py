from page_objects import iPhonePage


def test_add_cart(browser):
    iPhonePage(browser).go_site()
    assert iPhonePage(browser).add_to_cart() == iPhonePage(browser).CART_NAME
    iPhonePage(browser).close()


def test_device_name(browser):
    iPhonePage(browser).go_site()
    assert iPhonePage(browser).device_name() == iPhonePage(browser).NAME
    iPhonePage(browser).close()


def test_brand_name(browser):
    iPhonePage(browser).go_site()
    assert iPhonePage(browser).brand_name() == iPhonePage(browser).BRAND
    iPhonePage(browser).close()


def test_product_code(browser):
    iPhonePage(browser).go_site()
    assert iPhonePage(browser).product_code() == iPhonePage(browser).CODE
    iPhonePage(browser).close()


def test_availability(browser):
    iPhonePage(browser).go_site()
    assert iPhonePage(browser).availability_status() == iPhonePage(browser).STATUS
    iPhonePage(browser).close()
