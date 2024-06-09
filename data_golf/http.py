from data_golf.request_helpers import RequestHelpers

import httpx
import logging


class HttpClient:
    def __init__(self, config) -> None:
        self._config = config
        if self._config.verbose:
            logging.basicConfig(level=logging.INFO)

    def _build_url(self, resource: str, format: str):
        """
        Private method to build the URL for the Data Golf API.
        :param resource:
        :param format:
        :return:
        """
        params = [f"key={self._config.api_key}", f"file_format={format}"]
        url = ""

        if len(resource.split("?")) > 1:
            url = f"{self._config.base_url}{resource}&{'&'.join(params)}"
        else:
            url = f"{self._config.base_url}{resource}?{'&'.join(params)}"
        return url

    @RequestHelpers.prepare_request
    def get(self, resource: str, format: str = "json", **kwargs) -> httpx.request:
        """
        Private method to make a get request to the Data Golf API.  This wraps the lib httpx functionality.
        :param format:
        :param resource:
        :return:
        """
        with httpx.Client(
            verify=self._config.ssl_verify, timeout=self._config.timeout
        ) as client:
            r: httpx.request = client.get(
                url=self._build_url(resource, format), **kwargs
            )

        if self._config.verbose:
            logging.info(f"API URL: {r.url}")
            logging.info(kwargs["headers"])

        return r.json()
