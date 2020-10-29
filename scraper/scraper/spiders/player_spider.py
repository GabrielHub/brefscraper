import scrapy

class PSpider(scrapy.Spider):
    name = "players"
    
    #leaving room for more pages so you could get multiple years
    def start_requests(self):
        urls = [
            'https://www.basketball-reference.com/leagues/NBA_2020_per_game.html'
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    #full table should avoid duplicate players, but players who switched teams will have team TOT        
    def parse(self, response):
        for element in response.css('tr.full_table'):  
            yield {
                'name': self.get_string(element, 'td[data-stat="player"] a::text'),
                'position': self.get_string(element, 'td[data-stat="pos"]::text'),
                'age': self.get_stat(element, 'td[data-stat="age"]::text'),
                'team': self.get_string(element, 'td[data-stat="team_id"] a::text'),
                'games_played': self.get_stat(element, 'td[data-stat="g"]::text'),
                'games_started': self.get_stat(element, 'td[data-stat="gs"]::text'),
                'min_played': self.get_stat(element, 'td[data-stat="mp_per_g"]::text'),
                'fg': self.get_stat(element, 'td[data-stat="fg_per_g"]::text'),
                'fga': self.get_stat(element, 'td[data-stat="fga_per_g"]::text'),
                'fgp': self.get_stat(element, 'td[data-stat="fg_pct"]::text'),
                '3p': self.get_stat(element, 'td[data-stat="fg3_per_g"]::text'),
                '3pa': self.get_stat(element, 'td[data-stat="fg3a_per_g"]::text'),
                '3pp': self.get_stat(element, 'td[data-stat="fg3_pct"]::text'),
                '2p': self.get_stat(element, 'td[data-stat="fg2_per_g"]::text'),
                '2pa': self.get_stat(element, 'td[data-stat="fg2a_per_g"]::text'),
                '2pp': self.get_stat(element, 'td[data-stat="fg2_pct"]::text'),
                'efgp': self.get_stat(element, 'td[data-stat="efg_pct"]::text'),
                'ft': self.get_stat(element, 'td[data-stat="ft_per_g"]::text'),
                'fta': self.get_stat(element, 'td[data-stat="fta_per_g"]::text'),
                'ftp': self.get_stat(element, 'td[data-stat="ft_pct"]::text'),
                'orb': self.get_stat(element, 'td[data-stat="orb_per_g"]::text'),
                'drb': self.get_stat(element, 'td[data-stat="drb_per_g"]::text'),
                'trb': self.get_stat(element, 'td[data-stat="trb_per_g"]::text'),
                'ast': self.get_stat(element, 'td[data-stat="ast_per_g"]::text'),
                'stl': self.get_stat(element, 'td[data-stat="stl_per_g"]::text'),
                'blk': self.get_stat(element, 'td[data-stat="blk_per_g"]::text'),
                'tov': self.get_stat(element, 'td[data-stat="tov_per_g"]::text'),
                'pf': self.get_stat(element, 'td[data-stat="pf_per_g"]::text'),
                'pts': self.get_stat(element, 'td[data-stat="pts_per_g"]::text'),
                }
        
    #helper function extracts text from an html element, //td[@class="left "]/a/text()
    def get_string(self, response, selector):
        return ' '.join(response.css(selector).extract()).strip()
    
    def get_stat(self, response, selector):
        return response.css(selector).extract_first()