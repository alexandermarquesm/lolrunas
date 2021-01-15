import scrapy
from scrapy.crawler import CrawlerProcess
import ipdb


def parse_champion(response):
    champ = {
        'name': response.css('h1::text').get(),
        'rune': response.xpath(
            '//div[@class="perk-page__item perk-page__item--keystone perk-page__item--active"]//img/@alt').getall()[:1],
        'primaria': response.xpath('//div[@class="perk-page__item  perk-page__item--active"]//img/@alt').getall()[:3],
        'secundaria': response.xpath('//div[@class="perk-page__item perk-page__item--active"]//img/@alt').getall()[:2],
        'fragmento': response.xpath('//img[re:test(@class, "active")]/@alt').getall()[:3]
    }
    return champ


class MainSpider(scrapy.Spider):
    name = 'main-spider'

    start_urls = ['https://br.op.gg/champion/statistics']

    def parse(self, response):
        links = response.css('div[class=champion-index__champion-list] a::attr("href")').getall()
        for link in links:
            yield scrapy.Request(
                'https://br.op.gg' + link,
                callback=parse_champion
            )


process = CrawlerProcess()
process.crawl(MainSpider)
process.start()
