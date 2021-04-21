# -*- coding: utf-8 -*-
import re

import scrapy

from bossxr.items import JobItem
from bossxr.utils import SeleniumRequest


class BossSpider(scrapy.Spider):
    name = 'boss'
    start_url = (
        'https://www.zhipin.com/job_detail/?'
        'query=%E7%94%9F%E7%89%A9%E4%BF%A1%E6%81%AF&'
        'city={city}&industry=&position='
    )

    def start_requests(self):
        city = self.settings['BOSS_CITY']
        start_url = self.start_url.format(city=city)
        yield SeleniumRequest(url=start_url, callback=self.parse, wait_time=5)

    def parse(self, response):
        for li in response.xpath('//div[@class="job-list"]/ul/li'):
            item = JobItem()
            item['job_name'] = li.xpath('.//span[@class="job-name"]/a/text()').extract_first()
            salary_text = li.xpath(
                './/div[contains(@class, "job-limit")]/span[@class="red"]/text()'
            ).extract_first()
            temp = re.search(r'(?P<min>\d+)-(?P<max>\d+)K', salary_text)
            if temp:
                temp = temp.groupdict()
                item['min_salary'] = temp['min']
                item['max_salary'] = temp['max']
            else:
                item['min_salary'] = -1
                item['max_salary'] = -1
            item['company_name'] = li.xpath(
                './/div[@class="company-text"]/h3[@class="name"]/a/text()'
            ).extract_first()
            item['area'] = li.xpath(
                './/span[@class="job-area-wrapper"]/span[@class="job-area"]/text()'
            ).extract_first()
            yield item
        next_url = response.xpath(
            '//div[@class="page"]/a[contains(@class, "next")]/@href'
        ).extract_first()
        if next_url != 'javascript:;':
            next_url = response.urljoin(next_url)
            yield SeleniumRequest(url=next_url, callback=self.parse, wait_time=5)
