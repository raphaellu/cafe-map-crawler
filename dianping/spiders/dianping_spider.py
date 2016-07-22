import scrapy
from dianping.items import DianpingItem

from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

class DianpingSpider(scrapy.Spider):
    name = "dianping"
    allowed_domains = ["dianping.com"]
    start_urls = [
         "http://www.dianping.com/search/category/1/10/r8847"
        # "http://www.dianping.com/search/category/1/10/r5",
        # "http://www.dianping.com/search/category/1/10/r10"
    ]
        # "http://www.dianping.com/search/category/1/10/r5",
        # "http://www.dianping.com/search/category/1/10/r10",
        # "http://www.dianping.com/search/category/1/10/r5939",
        # "http://www.dianping.com/search/category/1/10/r2",
        # "http://www.dianping.com/search/category/1/10/r7",
        # "http://www.dianping.com/search/category/1/10/r8846",
        # "http://www.dianping.com/search/category/1/10/r6",
        # "http://www.dianping.com/search/category/1/10/r9",
        # "http://www.dianping.com/search/category/1/10/r8847",
        # "http://www.dianping.com/search/category/1/10/r1",
        # "http://www.dianping.com/search/category/1/10/r13",
        # "http://www.dianping.com/search/category/1/10/c3580",
        # "http://www.dianping.com/search/category/1/10/r3",
        # "http://www.dianping.com/search/category/1/10/r8",
        # "http://www.dianping.com/search/category/1/10/r4",
        # "http://www.dianping.com/search/category/1/10/r5937",
        # "http://www.dianping.com/search/category/1/10/r12",

    def parse(self, response):
        # print "====="
        # print response
        # print response.xpath("//@region-nav-sub")
        for href in response.xpath('//div[@id="region-nav-sub"]//@href').extract()[1:]:
            url = response.urljoin(href)
            # print url
            yield scrapy.Request(url, callback=self.parse_page_contents)

    def parse_page_contents(self, response):
        for sel in response.xpath('//div[@id="shop-all-list"]/ul/li'):
            item = DianpingItem()

            title = sel.css('.txt .tit a h4').xpath('text()').extract()
            if len(title) >= 1:
                item['title'] = title[0]
            else:
                item['title'] = '-'

            comment_price = sel.css('.txt .comment a b').xpath('text()').extract()
            if len(comment_price) >= 1:
                item['num_comment'] = comment_price[0]
            else:
                item['num_comment'] = '-'

            if len(comment_price) >= 2:
                item['price'] = sel.css('.txt .comment a b').xpath('text()').extract()[1][1:]
            else:
                item['price'] = '-'

            type_area = sel.css('.txt .tag-addr a span').xpath('text()').extract()
            if len(type_area) >= 1:
                item['dish_type'] = type_area[0]
            else:
                item['dish_type'] = '-'

            if len(type_area) >= 2:
                item['area'] = type_area[1]
            else:
                item['area'] = '-'

            addr = sel.css('.txt .tag-addr .addr').xpath('text()').extract()
            if len(addr) >= 1:
                item['addr'] = addr[0]
            else:
                item['addr'] = '-'

            rate = sel.css('.txt .comment-list span b').xpath('text()').extract()
            if len(rate) >= 3:
                item['flavor_rate'] = rate[0]
                item['env_rate'] = rate[1]
                item['srv_rate'] = rate[2]
            else:
                item['flavor_rate'] = '-'
                item['env_rate'] = '-'
                item['srv_rate'] = '-'
            yield item

        next_page = response.css('div .page .next').xpath('@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse_page_contents)

