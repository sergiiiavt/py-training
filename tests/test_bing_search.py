import re
from playwright.sync_api import Page, expect
from pages.bing_search_page import BingSearchPage


def test_bing_search(page: Page):
    bing_search_page = BingSearchPage(page)
    bing_search_page.open()
    bing_search_page.search("playwright")
    new_page = bing_search_page.open_first_result()
    expect(new_page).to_have_url(re.compile(r"playwright\.dev"))