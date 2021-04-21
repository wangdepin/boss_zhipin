# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    job_name = scrapy.Field()
    min_salary = scrapy.Field()
    max_salary = scrapy.Field()
    company_name = scrapy.Field()
    area = scrapy.Field()
