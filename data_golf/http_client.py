from typing import Tuple

from data_golf.request_helpers import RequestHelpers

import httpx
import logging


class DGForbidden(Exception):
    pass


class DGBadRequest(Exception):
    pass


class HttpClient:
    def __init__(self, config) -> None:
        self._config = config
        if self._config.verbose:
            logging.basicConfig(level=logging.INFO)

    def _build_request(
        self, resource: str, query_params: dict, format: str
    ) -> Tuple[str, dict]:
        """
        Private method to build the URL for the Data Golf API.
        :param resource:
        :param format:
        :return:
        """
        query_params["key"] = self._config.api_key
        query_params["file_format"] = format

        url = f"{self._config.base_url}{resource}?"

        return url, query_params

    @RequestHelpers.prepare_request
    def get(
        self, resource: str, params: dict = None, format: str = "json", **kwargs
    ) -> httpx.request:
        """
        Private method to make a get request to the Data Golf API.  This wraps the lib httpx functionality.
        :param params:
        :param format:
        :param resource:
        :return:
        """
        with httpx.Client(
            verify=self._config.ssl_verify, timeout=self._config.timeout
        ) as client:
            url, q = self._build_request(
                resource=resource, query_params=params if params else {}, format=format
            )
            r: httpx.request = client.get(
                url=url,
                params=q,
                **kwargs,
            )

        if r.status_code == 403:
            raise DGForbidden("403 Forbidden: Check your API key.")

        if r.status_code == 400:
            raise DGBadRequest(r.content)

        if self._config.verbose:
            logging.info(f"API URL: {r.url}")
            logging.info(kwargs["headers"])

        return r.json()
