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
                }
        
    #helper function extracts text from an html element, //td[@class="left "]/a/text()
    def get_string(self, response, selector):
        return ' '.join(response.css(selector).extract()).strip()
    
    def get_stat(self, response, selector):
        return response.css(selector).extract_first()