from data_golf.request_helpers import RequestHelpers

import httpx
import logging


class HttpClient:
    def __init__(self, config) -> None:
        self._config = config
        if self._config.verbose:
            logging.basicConfig(level=logging.INFO)

    def _build_url(self, resource: str, query_params: dict, format: str):
        """
        Private method to build the URL for the Data Golf API.
        :param resource:
        :param format:
        :return:
        """
        query_params["key"] = self._config.api_key
        query_params["file_format"] = format

        url = f"{self._config.base_url}{resource}?"

        url = self._append_query_params(query_params=query_params, url=url)

        return url

    def _append_query_params(self, query_params: dict, url: str) -> str:
        """
        Private method to append query parameters to the URL.
        :param query_params:
        :param url:
        :return:
        """
        if query_params:
            for k, v in query_params.items():
                url += f"&{k}={v}"
        return url

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
            r: httpx.request = client.get(
                url=self._build_url(
                    resource=resource,
                    query_params=params if params else {},
                    format=format,
                ),
                **kwargs,
            )

        if self._config.verbose:
            logging.info(f"API URL: {r.url}")
            logging.info(kwargs["headers"])

        return r.json()
