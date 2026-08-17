import re
import allure

from playwright.sync_api import Page, expect
from pages.bing_search_page import BingSearchPage


@allure.title("Search Playwright in Bing")
@allure.feature("Search")
def test_bing_search(page: Page):
    bing_page = BingSearchPage(page)

    bing_page.open()
    bing_page.search("playwright")

    new_page = bing_page.open_first_result()

    with allure.step("Verify the URL of the first search result"):
        expect(new_page).to_have_url(re.compile(r"playwright\.dev"))
