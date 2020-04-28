from page_objects import SearchPage


def test_search_page(browser, tim):
    SearchPage(browser,tim).go_site()
    assert SearchPage(browser, tim).search_name() == "Search - htc"
    SearchPage(browser, tim).input_search()
    SearchPage(browser, tim).category()
    SearchPage(browser, tim).limit()
    SearchPage(browser, tim).compare()
    SearchPage(browser, tim).close()