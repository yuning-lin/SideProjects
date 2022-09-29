from scrapyscript import Job, Processor
from crawler.spiders.lottery import LotterySpider
from scrapy.crawler import CrawlerProcess
import json
import pandas as pd

process = CrawlerProcess(settings={
    "FEEDS": {
        "result.json": {"format": "json"},
    },
})

process.crawl(LotterySpider)
process.start()

f = open('result.json')
data = json.load(f)
final_lst = []
for i in data:
    final_lst.append(pd.DataFrame(i))

final_df = pd.concat(final_lst)
final_df = final_df.sort_values(by='period')
final_df = final_df.reset_index(drop=True)
final_df = final_df.drop_duplicates()
final_df.to_csv('result.csv', index=False)