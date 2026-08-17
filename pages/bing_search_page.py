from playwright.sync_api import Page


class BingSearchPage:

    def __init__(self, page: Page):
        self.page = page

        self.search_box = page.locator("#sb_form_q")
        self.search_results = page.locator("li.b_algo h2 a")

    def open(self):
        self.page.goto("https://www.bing.com")

    def search(self, text: str):
        self.search_box.fill(text)
        self.search_box.press("Enter")

    def open_first_result(self) -> Page:
        with self.page.context.expect_page() as new_page_info:
            self.search_results.first.click()

        new_page = new_page_info.value
        new_page.wait_for_load_state()

        return new_page