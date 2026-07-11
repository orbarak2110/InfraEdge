from config.settings import SECTION_TITLE


def test_wikipedia_ui_word_counts(infra_edge_flow):
    title = infra_edge_flow.ui_flow.wikipedia_page.get_section_title()
    content = infra_edge_flow.ui_flow.wikipedia_page.get_section_content()
    word_counts = infra_edge_flow.utils.count_words(title, content)

    assert title == SECTION_TITLE, (
        f"Expected section title '{SECTION_TITLE}', "
        f"but got '{title}'"
    )
    assert content, "Section content should not be empty"
    assert word_counts, "Word counts should not be empty"