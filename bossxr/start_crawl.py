# -*- coding: utf-8 -*-
import click
from scrapy.crawler import CrawlerProcess

from bossxr.spiders.boss import BossSpider


SETTINGS = {
    'BOT_NAME': 'bossxr',
    'SPIDER_MODULES': ['bossxr.spiders'],
    'NEWSPIDER_MODULE': 'bossxr.spiders',
    'ROBOTSTXT_OBEY': False,
    'DOWNLOADER_MIDDLEWARES': {
        'bossxr.middlewares.SeleniumMiddleware': 543,
    },
    'SELENIUM_DRIVER_ARGUMENTS': [],
}


@click.command(name='bossxr')
@click.option(
    '-c', '--city', default='101010100',
    help='城市ID', show_default=True
)
@click.option(
    '-d', '--driver-name', default='chrome',
    help='驱动名称', show_default=True
)
@click.option(
    '-p', '--driver-path', default='/usr/local/bin/chromedriver',
    help='驱动路径', show_default=True
)
@click.option(
    '-p', '--proxy', default='http://127.0.0.1:6152',
    help='代理地址', show_default=True
)
@click.option(
    '-o', '--outfile', default='bossxr.json',
    help='输出文件（json格式）', show_default=True
)
def main(city, driver_name, driver_path, proxy, outfile):
    settings = {
        'BOSS_CITY': city,
        'SELENIUM_DRIVER_NAME': driver_name,
        'SELENIUM_DRIVER_EXECUTABLE_PATH': driver_path,
        'SELENIUM_DESIRED_CAPABILITIES': {
            'proxy': {
                'httpProxy': proxy,
                'sslProxy': proxy,
                'proxyType': 'MANUAL'
            }
        },
        'FEEDS': {
            outfile: {
                'format': 'jsonlines',
            }
        }
    }
    settings.update(SETTINGS)
    process = CrawlerProcess(settings)
    process.crawl(BossSpider)
    process.start()
    return 0


if __name__ == '__main__':
    main()
