import pytest
from playwright.sync_api import Page

from pages.bing_search_page import BingSearchPage


@pytest.fixture
def bing_page(page: Page) -> BingSearchPage:
    return BingSearchPage(page)
