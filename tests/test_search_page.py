""" bbb"""
from page_objects import SearchPage


def test_search_page(remote):
    """ aaa"""
    SearchPage(remote).go_site()
    assert SearchPage(remote).search_name() == "Search - htc"
    SearchPage(remote).input_search()
    SearchPage(remote).category()
    SearchPage(remote).limit()
    SearchPage(remote).compare()
    SearchPage(remote).close()
