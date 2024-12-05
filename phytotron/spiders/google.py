from datetime import date, timedelta
from typing import Any, Iterable

from scrapy.http.response import Response
from scrapy.spiders import Spider
from twisted.python.failure import Failure

from phytotron.items import PhytotronItem


class GoogleSpider(Spider):
    name = "google"

    def __init__(
        self,
        data: dict[str, Any],
        days: int,
        keywords: list[str],
        **kwargs: Any,
    ):
        super().__init__(**kwargs)
        self.data = data
        self.start_urls = [
            f"""https://www.google.com/search?q=site%3A"https%3A%2F%2Fboards.greenhouse.io"+%26+after%3A{
                date.today() - timedelta(days=days)
            }+%26+(united+states)+({
                ")+(".join(keyword.replace(" ", "+") for keyword in keywords)
            })"""
        ]

    def parse(self, response: Response, **_: Any) -> Any:
        urls = response.css("div#main div div div a::attr(href)").getall()
        for url in urls:
            yield response.follow(url, callback=self.parse_board)

        next_url = response.css("footer div:nth-child(1) div div a::attr(href)").get()
        if next_url:
            yield response.follow(next_url, callback=self.parse)

    def parse_board(self, response: Response) -> Iterable[PhytotronItem]:
        data = self.data

        # TODO: insert input into params from data for each field
        params = {}

        labels = response.xpath("//label").xpath("string()").getall()
        for label in labels:
            label = label.strip()
            if "*" in label:
                yield PhytotronItem(
                    url=response.url,
                    label=label.strip(),
                    input="",
                )

        # response.follow(response.url, method="POST", errback=self.errback_board)

    def errback_board(self, failure: Failure):
        pass
