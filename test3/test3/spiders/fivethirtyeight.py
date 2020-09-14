# -*- coding: utf-8 -*-
import scrapy
#import pdb;


class fivethirtyeightSpider(scrapy.Spider):

    #pdb.set_trace()
    name = 'fivethirtyeightSpider'
    allowed_domains = ['https://projects.fivethirtyeight.com/2020-mlb-predictions/games/']
    start_urls = ['https://projects.fivethirtyeight.com/2020-mlb-predictions/games/']

    def __init__(self, fulldate='', *args, **kwargs):
        super(fivethirtyeightSpider, self).__init__(*args, **kwargs)
        

    def parse(self, response):
        parser = scrapy.Selector(response)

        #Create array with selectors for each league
        XPATH_TEAMNAMES = "//a[contains(@class, 'team-link')]/span[contains(@class,'long')]/text()"
        XPATH_PITCHERS = "//span[contains(@class, 'pitcher-name')]/text()"  
        XPATH_TEAMRATING = "//td[@class='td number td-number rating']/text()"    
        XPATH_ADJRATING = "//td[@class='td number td-number rating-adj']"
        XPATH_WINCHANCE = "//td[@class='td number td-number win-prob']"

        raw_team_names = response.xpath(XPATH_TEAMNAMES).extract()
        raw_pitchers = response.xpath(XPATH_PITCHERS).extract()
        raw_team_ratings = response.xpath(XPATH_TEAMRATING).extract()
        raw_adj_ratings = response.xpath(XPATH_ADJRATING).extract()
        raw_win_chance = response.xpath(XPATH_WINCHANCE).extract()

        #Cleaning

        clean_adj_ratings = [0] * len(raw_adj_ratings)
        clean_win_chance =  [0] * len(raw_win_chance)


        for i in range(len(raw_adj_ratings)):
            clean_adj_ratings[i] = raw_adj_ratings[i][94:98]
            clean_win_chance[i] = raw_win_chance[i].split(')">')[1].split("</td")[0]



        for i in range(len(raw_team_names)):
            yield{
                'team': raw_team_names[i],
                'pitcher': raw_pitchers[i],
                'team rating': raw_team_ratings[i],
                'adjusted rating': clean_adj_ratings[i],
                'win chance': clean_win_chance[i]
            }

        
