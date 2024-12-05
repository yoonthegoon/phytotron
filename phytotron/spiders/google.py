from datetime import date, timedelta
from typing import Any

import scrapy
from scrapy.http import Response


class GoogleSpider(scrapy.Spider):
    name = "google"

    def __init__(
            self,
            keywords: list[str],
            location: str = "united states",
            days: int = 1,
            **kwargs: Any,
    ):
        super().__init__(**kwargs)

        if isinstance(keywords, str):
            keywords = keywords.split(",")

        if isinstance(days, str):
            days = int(days)

        self.start_urls = [
            f"""https://www.google.com/search?q=site%3A"https%3A%2F%2Fboards.greenhouse.io"+%26+after%3A{
                date.today() - timedelta(days=days)
            }+%26+({
                location.replace(" ", "+")
            })+{
                "+".join(keywords)
            }"""
        ]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        urls = response.css("div#main > div > div > div > a::attr(href)").getall()
        for url in urls:
            yield response.follow(url, callback=self.parse_board)

        next_url = response.css("footer > div:nth-child(1) > div > div > a::attr(href)").get()
        if next_url:
            yield response.follow(next_url, callback=self.parse)

    @staticmethod
    def parse_board(response: Response) -> Any:
        yield {"url": response.url}
        # TODO:
        #   - use pre-defined form data
        #   - fill in post data
        ...
