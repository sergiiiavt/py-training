import re

from playwright.sync_api import Page, expect


def test_google_search(page: Page):
    # Open Bing
    page.goto("https://www.bing.com")

    # Find search field
    search_box = page.locator("#sb_form_q")

    # Search
    search_box.fill("playwright")
    search_box.press("Enter")

    # Find first search result
    first_result = page.locator("li.b_algo h2 a").first

    # Bing opens search result in a new tab
    with page.context.expect_page() as new_page_info:
        first_result.click()

    new_page = new_page_info.value

    # Wait until the new page is loaded
    new_page.wait_for_load_state()

    # Check that Playwright site was opened
    expect(new_page).to_have_url(re.compile(r"playwright\.dev"))