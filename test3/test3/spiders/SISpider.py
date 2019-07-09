# -*- coding: utf-8 -*-
import scrapy


class SispiderSpider(scrapy.Spider):
    name = 'SISpider'
    allowed_domains = ['http://www.si.com/mlb/scoreboard']
    start_urls = ['http://www.si.com/mlb/scoreboard/']

    def parse(self, response):
        parser = scrapy.Selector(response)

        #Create array with selectors for each game
        XPATH_GAMES = "//div[@class='score-tile-large']"
        games = response.xpath(XPATH_GAMES)
        
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

