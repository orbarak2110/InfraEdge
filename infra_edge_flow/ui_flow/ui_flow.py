from playwright.sync_api import Page

from infra_edge_flow.ui_flow.pages.wikipedia_page import WikipediaPage


class UIFlow():
    def __init__(self, page: Page):
        self.wikipedia_page = WikipediaPage(page)