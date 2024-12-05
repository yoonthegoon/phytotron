import tomllib
from scrapy.crawler import CrawlerProcess

from phytotron.spiders.google import GoogleSpider

if __name__ == "__main__":
    with open("phytotron.toml", "rb") as f:
        data = tomllib.load(f)

    days: int = data["arguments"]["days"]
    keywords: list[str] = data["arguments"]["keywords"]

    # TODO: crawl GreenhouseSpider on rerun arg

    process = CrawlerProcess()
    process.crawl(GoogleSpider, data=data, days=days, keywords=keywords)
    process.start()
    process.stop()
