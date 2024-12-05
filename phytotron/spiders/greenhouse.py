from typing import Any

import scrapy
from scrapy.http.response import Response


class GreenhouseSpider(scrapy.Spider):
    name = "greenhouse"

    def __init__(self, data: dict[str, Any], *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.data = data
        self.start_urls = []  # TODO: read from items.csv probably with pandas or polars

    def parse(self, response: Response, **_: Any) -> Any:
        pass
