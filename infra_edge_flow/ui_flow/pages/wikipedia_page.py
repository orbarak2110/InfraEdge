import logging

from playwright.sync_api import Locator, Page

from config.settings import (
    SECTION_TITLE,
    WIKIPEDIA_PAGE_URL
)


logger = logging.getLogger(__name__)


class WikipediaPage:
    def __init__(self, page: Page):
        self.page = page

        self.section_title: Locator = self.page.locator(
            f"h3#{SECTION_TITLE.replace(' ', '_')}"
        )

        self.section_content: Locator = (
            self.section_title
            .locator("xpath=../following-sibling::p[1]")
        )

    def open(self) -> None:
        logger.info(
            "Opening Wikipedia page: %s",
            WIKIPEDIA_PAGE_URL
        )

        self.page.goto(
            WIKIPEDIA_PAGE_URL,
            wait_until="domcontentloaded"
        )

    def get_section_title(self) -> str:
        section_title = self.section_title.inner_text().strip()

        logger.info(
            "Section title: %s",
            section_title
        )

        return section_title

    def get_section_content(self) -> str:
        section_content = self.section_content.inner_text().strip()

        logger.info(
            "Section content: %s",
            section_content
        )

        return section_content