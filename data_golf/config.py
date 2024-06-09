class DGConfig:
    def __init__(
        self,
        api_key: str,
        verbose: bool = False,
        timeout: int = 15,
        ssl_verify: bool = True,
    ) -> None:
        self.api_key = api_key
        self.verbose = verbose
        self.timeout = timeout
        self.ssl_verify = ssl_verify
        self.base_url = "https://feeds.datagolf.com"
