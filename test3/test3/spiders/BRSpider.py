# -*- coding: utf-8 -*-
import scrapy

#Copied xpath AL records: //*[@id="standings-upto-AL-overall"]/tbody
#Copied xpath NL records: //*[@id="standings-upto-NL-overall"]/tbody

class BRSpider(scrapy.Spider):
    name = 'BRSpider'
    allowed_domains = ['https://www.baseball-reference.com/boxes/?month=10&day=9&year=2011']
    start_urls = ['https://www.baseball-reference.com/boxes/?month=10&day=9&year=2011]

    def parse(self, response):
        parser = scrapy.Selector(response)

        #Create array with selectors for each league
        XPATH_ALGAMES = "//*[@id='standings-upto-AL-overall']/tbody"
        XPATH_NLGAMES = "//*[@id='standings-upto-NL-overall']/tbody"
        ALgames = response.xpath(XPATH_ALGAMES)
        NLgames = response.xpath(XPATH_NLGAMES)

	#Xpaths for specific data
	XPATH_CITY = "//th/a"
	XPATH_GB = "//td[4]"
	XPATH_RS = "//td[5]"
	XPATH_RA = "//td[6]"
	XPATH_WINS = "//td[1]"
	XPATH_LOSSES = "//td[2]"
	XPATH_WINPER = "//td[3]"

	for game in ALgames:

            raw_city = game.xpath(XPATH_CITY).extract()
	    raw_GB = game.xpath(XPATH_GB).extract()
	    raw_RS = game.xpath(XPATH_RS).extract()
	    raw_RA = game.xpath(XPATH_RA).extract()
            raw_wins = game.xpath(XPATH_WINS).extract()
	    raw_losses = game.xpath(XPATH_LOSSES).extract()
	    raw_winPer = game.xpath(XPATH_WINPER).extract()

        yield{
                'city': raw_city[0],
                'GB': raw_GB[0],
                'RS': raw_RS[0],
                'RA': raw_RA[0]
		'wins': raw_wins[0]
		'losses': raw_losses[0]
		'winper': raw_winPer[0]
	    }

        

'''
        #XPaths for each statistic needed
        XPATH_CITY = "./div[@class='teams']/div[contains(@class, 'media')]/div[@class='team-name-container ']/div[@class='team-city']/a[@class='unskinned']"
        XPATH_SCORE = "./div[@class='teams']/div[contains(@class, 'media')]/div[contains(@class, 'media')]/div[contains(@class, 'team-score')]"

	#for each game, extract each statistic and clean
        for game in games:

            #get raw text from html
            raw_city = game.xpath(XPATH_CITY).extract()
            raw_score = game.xpath(XPATH_SCORE).extract()
            
            #clean city data
            split_city1 = raw_city[0].split() 
            if split_city1[5] == "</a>":
                clean_city1 = split_city1[4]
            else:
                clean_city1 = split_city1[4] + " " + split_city1[5]
            split_city_2 = raw_city[1].split() 
            if split_city_2[5] == "</a>":
                clean_city2 = split_city_2[4]
            else:
                clean_city2 = split_city_2[4] + " " + split_city_2[5]


            #clean score data
            split_score1 = raw_score[0].split() if raw_score else None
            clean_score1 = split_score1[3] if split_score1 else None
            split_score2 = raw_score[1].split() if raw_score else None
            clean_score2 = split_score2[3] if split_score2 else None

            #outputs for csv
            yield{
                'team1_city': clean_city1,
                'team2_city': clean_city2,
                'team1_score': clean_score1,
                'team2_score': clean_score2
	    }

'''

