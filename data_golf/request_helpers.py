from functools import wraps

ALLOWED_FORMATS = ["json"]


class RequestHelpers:

    @classmethod
    def _set_headers(cls, f_format) -> dict[str, str]:
        headers = {}
        if f_format not in ALLOWED_FORMATS:
            raise ValueError("format must be 'json'.  CSV support is coming")

        if f_format == "json":
            headers["Content-Type"] = "application/json"
        elif f_format == "csv":
            headers["Content-Type"] = "text/csv; charset=utf-8"

        return headers

    @staticmethod
    def prepare_request(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            f_format = kwargs.get("format", "json")

            headers = RequestHelpers._set_headers(f_format=f_format)

            kwargs["headers"] = {**kwargs.get("headers", {}), **headers}
            return func(*args, **kwargs)

        return wrapper
