import scrapy
# from scrapy_selenium import SeleniumRequest
from scrapy.http import Request, FormRequest
from crawler.items import CrawlerItem


class LotterySpider(scrapy.Spider):
    name = 'lottery'
    allowed_domains = ['www.taiwanlottery.com.tw']
    start_urls = ['https://www.taiwanlottery.com.tw/lotto/3D/history.aspx']

    def parse(self, response):
        for y in range(103, 112): 
            for m in range(1, 13):
                yield FormRequest.from_response(response,
                                                formdata={'L3DControl_history1$chk': 'radYM',
                                                          'L3DControl_history1$dropYear': f'{y}',
                                                          'L3DControl_history1$dropMonth':f'{m}',
                                                          'L3DControl_history1$btnSubmit':'查詢'},
                                                callback=self.parse_pages)
    
    def parse_pages(self, response):
        item = CrawlerItem()
        item['period'] = response.selector.xpath(f'//table[@class="table_org"]//tr[3]/td[1]//text()').getall()
        item['lottery_date'] = response.selector.xpath(f'//table[@class="table_org"]//tr[3]/td[2]//text()[2]').getall()
        item['num1'] = response.selector.xpath(f'//table[@class="table_org"]//tr[3]/td[3]/span[1]/text()').getall()
        item['num2'] = response.selector.xpath(f'//table[@class="table_org"]//tr[3]/td[3]/span[2]/text()').getall()
        item['num3'] = response.selector.xpath(f'//table[@class="table_org"]//tr[3]/td[3]/span[3]/text()').getall()
        item['sales_amt'] = response.selector.xpath(f'//table[@class="table_org"]//tr[3]/td[9]//text()[2]').getall()
        item['deadline_date'] = response.selector.xpath(f'//table[@class="table_org"]//tr[4]/td[1]//text()[2]').getall()
        item['prize1'] = response.selector.xpath(f'//table[@class="table_org"]//tr[4]/td[4]/text()').getall()
        item['prize2'] = response.selector.xpath(f'//table[@class="table_org"]//tr[4]/td[5]/text()').getall()
        item['prize3'] = response.selector.xpath(f'//table[@class="table_org"]//tr[4]/td[6]/text()').getall()
        item['prize4'] = response.selector.xpath(f'//table[@class="table_org"]//tr[4]/td[7]/text()').getall()
        item['prize_amt'] = response.selector.xpath(f'//table[@class="table_org"]//tr[4]/td[8]//text()[2]').getall()
        
        item['period'] += response.selector.xpath(f'//table[@class="table_gre"]//tr[3]/td[1]//text()').getall()
        item['lottery_date'] += response.selector.xpath(f'//table[@class="table_gre"]//tr[3]/td[2]//text()[2]').getall()
        item['num1'] += response.selector.xpath(f'//table[@class="table_gre"]//tr[3]/td[3]/span[1]/text()').getall()
        item['num2'] += response.selector.xpath(f'//table[@class="table_gre"]//tr[3]/td[3]/span[2]/text()').getall()
        item['num3'] += response.selector.xpath(f'//table[@class="table_gre"]//tr[3]/td[3]/span[3]/text()').getall()
        item['sales_amt'] += response.selector.xpath(f'//table[@class="table_gre"]//tr[3]/td[9]//text()[2]').getall()
        item['deadline_date'] += response.selector.xpath(f'//table[@class="table_gre"]//tr[4]/td[1]//text()[2]').getall()
        item['prize1'] += response.selector.xpath(f'//table[@class="table_gre"]//tr[4]/td[4]/text()').getall()
        item['prize2'] += response.selector.xpath(f'//table[@class="table_gre"]//tr[4]/td[5]/text()').getall()
        item['prize3'] += response.selector.xpath(f'//table[@class="table_gre"]//tr[4]/td[6]/text()').getall()
        item['prize4'] += response.selector.xpath(f'//table[@class="table_gre"]//tr[4]/td[7]/text()').getall()
        item['prize_amt'] += response.selector.xpath(f'//table[@class="table_gre"]//tr[4]/td[8]//text()[2]').getall()
        
        yield item