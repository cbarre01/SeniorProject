# -*- coding: utf-8 -*-
import scrapy


class BrspiderSpider(scrapy.Spider):
    name = 'BRSpider'
    allowed_domains = ['https://www.baseball-reference.com/boxes/?month=10&day=9&year=2011']
    start_urls = ['https://www.baseball-reference.com/boxes/?month=10&day=9&year=2011']

    def parse(self, response):
        parser = scrapy.Selector(response)

        #Create array with selectors for each league
        XPATH_ALGAMES = "//*[@id='standings-upto-AL-overall']/tbody"
        XPATH_NLGAMES = "//*[@id='standings-upto-NL-overall']/tbody"
        ALgames = response.xpath(XPATH_ALGAMES)
        NLgames = response.xpath(XPATH_NLGAMES)

        #Extraction from html for AL teams
        XPATH_CITY_AL = XPATH_ALGAMES + "//th/a"
        XPATH_GB_AL = XPATH_ALGAMES + "//td[4]"
        XPATH_RS_AL = XPATH_ALGAMES + "//td[5]"
        XPATH_RA_AL = XPATH_ALGAMES + "//td[6]"
        XPATH_WINS_AL = XPATH_ALGAMES + "//td[1]"
        XPATH_LOSSES_AL = XPATH_ALGAMES + "//td[2]"
        XPATH_WINPER_AL = XPATH_ALGAMES + "//td[3]"

        raw_cities_AL = response.xpath(XPATH_CITY_AL).extract()
        raw_GBs_AL = response.xpath(XPATH_GB_AL).extract()
        raw_RSs_AL = response.xpath(XPATH_RS_AL).extract()
        raw_RAs_AL = response.xpath(XPATH_RA_AL).extract()
        raw_wins_AL = response.xpath(XPATH_WINS_AL).extract()
        raw_losses_AL = response.xpath(XPATH_LOSSES_AL).extract()
        raw_winPer_AL = response.xpath(XPATH_WINPER_AL).extract()

        clean_cities_AL = [0] * len(raw_cities_AL)
        clean_RSs_AL = [0] * len(raw_cities_AL)
        clean_RAs_AL = [0] * len(raw_cities_AL)
        clean_GBs_AL = [0] * len(raw_cities_AL)
        clean_wins_AL = [0] * len(raw_cities_AL)
        clean_losses_AL = [0] * len(raw_cities_AL)
        clean_winPer_AL = [0] * len(raw_cities_AL)


        #parsing/cleaning strings for AL
        for i in range(len(raw_cities_AL)):
            clean_cities_AL[i] = raw_cities_AL[i][32:35]
            clean_RSs_AL[i] = raw_RSs_AL[i][34:38]
            clean_RSs_AL[i] = ''.join(c for c in clean_RSs_AL[i] if c.isdigit())
            clean_RAs_AL[i] = raw_RAs_AL[i][34:38]
            clean_RAs_AL[i] = ''.join(c for c in clean_RAs_AL[i] if c.isdigit())
            clean_wins_AL[i] = raw_wins_AL[i][33:36]
            clean_wins_AL[i] = ''.join(c for c in clean_wins_AL[i] if c.isdigit())
            clean_losses_AL[i] = raw_losses_AL[i][33:36]
            clean_losses_AL[i] = ''.join(c for c in clean_losses_AL[i] if c.isdigit())
            clean_winPer_AL[i] = raw_winPer_AL[i][45:49]

        clean_GBs_AL[0] = 0.0
        for i in range(1,len(raw_GBs_AL)):
            clean_GBs_AL[i] = raw_GBs_AL[i][43:46]

        #Extraction from html for NL teams
        XPATH_CITY_NL = XPATH_NLGAMES + "//th/a"
        XPATH_GB_NL = XPATH_NLGAMES + "//td[4]"
        XPATH_RS_NL = XPATH_NLGAMES + "//td[5]"
        XPATH_RA_NL = XPATH_NLGAMES + "//td[6]"
        XPATH_WINS_NL = XPATH_NLGAMES + "//td[1]"
        XPATH_LOSSES_NL = XPATH_NLGAMES + "//td[2]"
        XPATH_WINPER_NL = XPATH_NLGAMES + "//td[3]"

        raw_cities_NL = response.xpath(XPATH_CITY_NL).extract()
        raw_GBs_NL = response.xpath(XPATH_GB_NL).extract()
        raw_RSs_NL = response.xpath(XPATH_RS_NL).extract()
        raw_RAs_NL = response.xpath(XPATH_RA_NL).extract()
        raw_wins_NL = response.xpath(XPATH_WINS_NL).extract()
        raw_losses_NL = response.xpath(XPATH_LOSSES_NL).extract()
        raw_winPer_NL = response.xpath(XPATH_WINPER_NL).extract()

        clean_cities_NL = [0] * len(raw_cities_NL)
        clean_RSs_NL = [0] * len(raw_cities_NL)
        clean_RAs_NL = [0] * len(raw_cities_NL)
        clean_GBs_NL = [0] * len(raw_cities_NL)
        clean_wins_NL = [0] * len(raw_cities_NL)
        clean_losses_NL = [0] * len(raw_cities_NL)
        clean_winPer_NL = [0] * len(raw_cities_NL)

        #parsing/cleaning strings for NL
        for i in range(len(raw_cities_NL)):
            clean_cities_NL[i] = raw_cities_NL[i][32:35]
            clean_RSs_NL[i] = raw_RSs_NL[i][34:38]
            clean_RSs_NL[i] = ''.join(c for c in clean_RSs_NL[i] if c.isdigit())
            clean_RAs_NL[i] = raw_RAs_NL[i][34:38]
            clean_RAs_NL[i] = ''.join(c for c in clean_RAs_NL[i] if c.isdigit())
            clean_wins_NL[i] = raw_wins_NL[i][33:36]
            clean_wins_NL[i] = ''.join(c for c in clean_wins_NL[i] if c.isdigit())
            clean_losses_NL[i] = raw_losses_NL[i][33:36]
            clean_losses_NL[i] = ''.join(c for c in clean_losses_NL[i] if c.isdigit())
            clean_winPer_NL[i] = raw_winPer_NL[i][45:49]

        clean_GBs_NL[0] = 0.0
        for i in range(1,len(raw_GBs_NL)):
            clean_GBs_NL[i] = raw_GBs_NL[i][43:46]

        clean_cities = clean_cities_AL + clean_cities_NL
        clean_RSs = clean_RSs_AL + clean_RSs_NL
        clean_RAs = clean_RAs_AL + clean_RAs_NL
        clean_wins = clean_wins_AL + clean_wins_NL
        clean_losses = clean_losses_AL + clean_losses_NL
        clean_winPer = clean_winPer_AL + clean_winPer_NL
        clean_GBs = clean_GBs_AL + clean_GBs_NL

        print("CITIES TEST##########:")
        print(clean_cities)

        for i in range(len(clean_cities)):
            yield{
                'city': clean_cities[i],
                'GB': clean_GBs[i],
                'RS': clean_RSs[i],
                'RA': clean_RAs[i],
                'wins': clean_wins[i],
                'losses': clean_losses[i],
                'winper': clean_winPer[i]
            }

        
