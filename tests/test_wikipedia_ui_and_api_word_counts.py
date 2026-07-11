from config.settings import SECTION_TITLE, WIKIPEDIA_PAGE_TITLE



def test_wikipedia_ui_and_api_word_counts(infra_edge_flow):
    """
        Compare the Wikipedia section word counts retrieved from the UI and API.

        The test retrieves the configured Wikipedia section title and content
        through the browser UI, retrieves the same section content through the
        Wikipedia API, and generates a word-count dictionary for both sources.

        The test verifies that:

        - The UI section title is not empty.
        - The UI section content is not empty.
        - The API section content is not empty.
        - The normalized UI and API word-count dictionaries are identical.
    """
    ui_section_title = infra_edge_flow.ui_flow.wikipedia_page.get_section_title()


    ui_section_content = infra_edge_flow.ui_flow.wikipedia_page.get_section_content()

    ui_word_counts = infra_edge_flow.utils.count_words(
        title=ui_section_title,
        content=ui_section_content,
        source="UI"
    )

    api_section_content = infra_edge_flow.api_flow.wikipedia_api.get_section_content(
            page_title=WIKIPEDIA_PAGE_TITLE,
            section_title=SECTION_TITLE
        )

    api_word_counts = infra_edge_flow.utils.count_words(
        title=SECTION_TITLE,
        content=api_section_content,
        source="API"
    )

    assert ui_section_title, "UI section title should not be empty"
    assert ui_section_content, "UI section content should not be empty"
    assert api_section_content, "API section content should not be empty"
    assert ui_word_counts == api_word_counts, (
        "UI and API word counts are different.\n"
        f"UI word counts: {ui_word_counts}\n"
        f"API word counts: {api_word_counts}"
    )