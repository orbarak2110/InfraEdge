import logging
import re
from collections import Counter


logger = logging.getLogger(__name__)


class Utils:
    @staticmethod
    def count_words(
        title: str,
        content: str,
        source: str = ""
    ) -> dict[str, int]:
        full_text = f"{title} {content}"

        logger.info(
            "%s full text before cleaning: %s",
            source,
            full_text
        )

        text_without_brackets = re.sub(
            r"\[[^\]]*]",
            "",
            full_text
        )

        logger.info(
            "%s text after removing brackets: %s",
            source,
            text_without_brackets
        )

        words = re.findall(
            r"[a-zA-Z0-9]+",
            text_without_brackets.casefold()
        )

        word_counts = dict(
            Counter(words)
        )

        logger.info(
            "%s word counts: %s",
            source,
            word_counts
        )

        logger.info(
            "%s unique words count: %d",
            source,
            len(word_counts)
        )

        for word in sorted(word_counts):
            logger.info(
                "%s | %s: %d",
                source,
                word,
                word_counts[word]
            )

        return word_counts