import logging

import requests


logger = logging.getLogger(__name__)


class BaseApi:
    def __init__(
        self,
        base_url: str,
        timeout: int = 10,
        headers: dict | None = None
    ):
        self.base_url = base_url
        self.timeout = timeout
        self.headers = headers or {}

    def get(
        self,
        params: dict | None = None,
        headers: dict | None = None
    ) -> dict:
        request_headers = {
            **self.headers,
            **(headers or {})
        }

        logger.info(
            "Sending GET request to %s with params: %s",
            self.base_url,
            params
        )

        response = requests.get(
            url=self.base_url,
            params=params,
            headers=request_headers,
            timeout=self.timeout
        )

        logger.info(
            "Response status code: %s",
            response.status_code
        )

        response.raise_for_status()

        return response.json()