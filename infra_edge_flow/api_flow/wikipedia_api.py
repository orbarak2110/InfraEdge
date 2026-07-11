import logging

from bs4 import BeautifulSoup

from config.settings import WIKIPEDIA_API_URL
from infra_edge_flow.api_flow.base_api import BaseApi


logger = logging.getLogger(__name__)


class WikipediaApi(BaseApi):
    def __init__(
        self,
        api_url: str = WIKIPEDIA_API_URL
    ):
        super().__init__(
            base_url=api_url,
            timeout=10,
            headers={
                "User-Agent": "InfraEdgeAutomation/1.0"
            }
        )

    def get_section_index(
        self,
        page_title: str,
        section_title: str
    ) -> str:
        params = {
            "action": "parse",
            "page": page_title,
            "prop": "sections",
            "format": "json",
            "formatversion": "2"
        }

        response_data = self.get(
            params=params
        )

        sections = response_data["parse"]["sections"]

        for section in sections:
            current_title = section["line"].strip()

            if (
                current_title.casefold()
                == section_title.strip().casefold()
            ):
                section_index = section["index"]

                logger.info(
                    "Found section '%s' with index %s",
                    current_title,
                    section_index
                )

                return section_index

        raise ValueError(
            f"Section '{section_title}' was not found "
            f"in Wikipedia page '{page_title}'"
        )

    def get_section_html(
        self,
        page_title: str,
        section_title: str
    ) -> str:
        section_index = self.get_section_index(
            page_title=page_title,
            section_title=section_title
        )

        params = {
            "action": "parse",
            "page": page_title,
            "section": section_index,
            "prop": "text",
            "format": "json",
            "formatversion": "2"
        }

        response_data = self.get(
            params=params
        )

        section_html = response_data["parse"]["text"]

        logger.info(
            "Received HTML for section '%s'",
            section_title
        )

        return section_html

    def get_section_content(
        self,
        page_title: str,
        section_title: str
    ) -> str:
        section_html = self.get_section_html(
            page_title=page_title,
            section_title=section_title
        )

        section_content = self._convert_html_to_text(
            section_html=section_html
        )

        logger.info(
            "API section content for '%s': %s",
            section_title,
            section_content
        )

        return section_content

    @staticmethod
    def _convert_html_to_text(
        section_html: str
    ) -> str:
        soup = BeautifulSoup(
            section_html,
            "html.parser"
        )

        elements_to_remove = [
            "sup.reference",
            ".mw-editsection",
            ".reflist",
            ".references",
            "ol.references",
            "script",
            "style"
        ]

        for selector in elements_to_remove:
            for element in soup.select(selector):
                element.decompose()

        section_heading = soup.find(
            ["h1", "h2", "h3", "h4", "h5", "h6"]
        )

        if section_heading:
            section_heading.decompose()

        section_content = soup.get_text(
            separator=" ",
            strip=True
        )

        return " ".join(
            section_content.split()
        )