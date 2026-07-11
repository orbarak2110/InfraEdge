import logging
from pathlib import Path

import pytest
from playwright.sync_api import Page

from config.settings import DEFAULT_TIMEOUT
from infra_edge_flow.infra_edge_flow import InfraEdgeFlow


logger = logging.getLogger(__name__)


@pytest.fixture(scope="module", autouse=True)
def log_by_test_file(request):
    test_file_name = Path(str(request.node.path)).stem

    log_file_path = (
        request.node.path.parent
        / f"{test_file_name}.log"
    )

    file_handler = logging.FileHandler(
        log_file_path,
        mode="w",
        encoding="utf-8"
    )

    file_handler.setLevel(logging.INFO)

    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(name)s | "
            "%(message)s"
        )
    )

    root_logger = logging.getLogger()
    previous_log_level = root_logger.level

    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)

    try:
        yield
    finally:
        root_logger.removeHandler(file_handler)
        root_logger.setLevel(previous_log_level)
        file_handler.close()


@pytest.fixture
def infra_edge_flow(page: Page):
    page.set_default_timeout(DEFAULT_TIMEOUT)

    flow = InfraEdgeFlow(page)

    flow.ui_flow.wikipedia_page.open()

    try:
        yield flow
    finally:
        logger.info(
            "Finished test on Wikipedia page"
        )