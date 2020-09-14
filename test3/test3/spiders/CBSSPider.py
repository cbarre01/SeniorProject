# -*- coding: utf-8 -*-
import scrapy
import numpy as np
#import pdb;


class CBSSpider(scrapy.Spider):

    #pdb.set_trace()
    name = 'CBSSpider'
    allowed_domains = ['https://www.cbssports.com/mlb/scoreboard/']
    start_urls = ['https://www.cbssports.com/mlb/scoreboard/']

    def __init__(self, fulldate='', *args, **kwargs):
        super(CBSSpider, self).__init__(*args, **kwargs)
        

    def parse(self, response):
        parser = scrapy.Selector(response)

        XPATH_TEAMS = "//div[@class='single-score-card  ingame mlb']//tbody/tr/td[@class='team']/a/text()"

        ##Scores stored in table, in below xpath home team name is in index 0 + 8(n - 1). Home score is 1 + 8(n -1). Away team name is 4 + 8(n-1), and away team score is 5 + 8(n-1) where n is the game number
        XPATH_HOMESCORE = "//div[@class='single-score-card  ingame mlb']//tbody/tr/td" 
        XPATH_AWAYSCORE = "//div[@class='single-score-card  ingame mlb']//tbody/tr/td"
        XPATH_INNING = 'https://www.cbssports.com/mlb/scoreboard/'

        tableData = response.xpath(XPATH_HOMESCORE).extract()


        numTeams = len(response.xpath(XPATH_TEAMS).extract())
        numGames = numTeams // 2

        #print(numTeams)

        raw_home_team = [-1] * numGames
        raw_away_team = [-1] * numGames
        clean_homescore = [-1] * numGames
        clean_awayscore = [-1] * numGames
        clean_inning = [-1] * numGames
 
        #print(raw_home_team)

        for i in range(len(response.xpath(XPATH_TEAMS).extract())):

            #print(i)
            #print(i//2)
            #print(raw_home_team[i // 2])
            #print(response.xpath(XPATH_TEAMS).extract()[i])
            
            if i % 2 == 0:
                raw_home_team[i // 2] = response.xpath(XPATH_TEAMS).extract()[i]
            else:
                raw_away_team[i // 2] = response.xpath(XPATH_TEAMS).extract()[i]

        for i in range(len(tableData)):
            if i % 8 == 1:
                clean_homescore[i // 8] = response.xpath(XPATH_AWAYSCORE).extract()[i]
            elif i % 8 == 5:
                clean_awayscore[i // 8] = response.xpath(XPATH_AWAYSCORE).extract()[i]
        
        for i in range(numGames):
            yield{
                'home': raw_home_team[i],
                'away': raw_away_team[i],
                'homescore': clean_homescore[i],
                'awayscore': clean_awayscore[i],
                #'inning': clean_win_chance[i]
            }
