from page_objects import SearchPage


def test_search_page():
    assert SearchPage().search_name() == "Search - htc"
    SearchPage().input_search()
    SearchPage().category()
    SearchPage().limit()
    SearchPage().compare()
    SearchPage().close()
