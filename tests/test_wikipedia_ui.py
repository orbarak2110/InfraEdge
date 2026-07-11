from config.settings import SECTION_TITLE


def test_wikipedia_ui_word_counts(infra_edge_flow):
    """
        Validate the Wikipedia section title, content, and generated word counts.

        The test retrieves the configured section title and content from the
        Wikipedia UI, creates a word-count dictionary from both values, and
        verifies that:

        - The actual section title matches the expected configured title.
        - The section content is not empty.
        - The generated word-count dictionary is not empty.
    """
    title = infra_edge_flow.ui_flow.wikipedia_page.get_section_title()
    content = infra_edge_flow.ui_flow.wikipedia_page.get_section_content()
    word_counts = infra_edge_flow.utils.count_words(title, content)

    assert title == SECTION_TITLE, (
        f"Expected section title '{SECTION_TITLE}', "
        f"but got '{title}'"
    )
    assert content, "Section content should not be empty"
    assert word_counts, "Word counts should not be empty"