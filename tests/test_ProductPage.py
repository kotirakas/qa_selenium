from selenium.common.exceptions import NoSuchElementException, TimeoutException
from page_objects import ProductPage


def test_product_page(browser, tim):
    ProductPage(browser, tim).go_site()
    try:
        ProductPage(browser, tim).wait_description()
        ProductPage(browser, tim).wait_add()
        ProductPage(browser, tim).wait_quantity()
        ProductPage(browser, tim).wait_review()
        ProductPage(browser, tim).wait_price()

    except NoSuchElementException:
        print("нет такого элемента")
    except TimeoutException:
        print("time is over")
    finally:
        ProductPage(browser, tim).close()
