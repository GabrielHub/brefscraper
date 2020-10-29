import json

#Player object that holds the scraped statistical data
class PlayerStat:
    def __init__(self, params):
        self.name = params.get('name')
        self.position = params.get('position')
        self.age = params.get('age')
        self.team = params.get('team')
        self.games_played = params.get('games_played')
        self.games_started = params.get('games_started')
        self.min_played = params.get('min_played')
        self._fg = params.get('fg')
        self._fga = params.get('fga')
        self._fgp = params.get('fgp')
        self._3p = params.get('3p')
        self._3pa = params.get('3pa')
        self._3pp = params.get('3pp')
        self._2p = params.get('2p')
        self._2pa = params.get('2pa')
        self._2pp = params.get('2pp')
        self.efgp = params.get('efgp')
        self.ft = params.get('ft')
        self.fta = params.get('fta')
        self.ftp = params.get('ftp')
        self.orb = params.get('orb')
        self.drb = params.get('drb')
        self.trb = params.get('trb')
        self.ast = params.get('ast')
        self.stl = params.get('stl')
        self.blk = params.get('blk')
        self.tov = params.get('tov')
        self.pf = params.get('pf')
        self.pts = params.get('pts')
        
#Turns scraped json data to python object
class PlayerPool:
    def __init__(self):
        self.pool = []
        
        #open json file
        with open("scraper/output.json", "r") as rfile:
            data = json.load(rfile)
        #load player data
        self.pool = [PlayerStat(p) for p in data]
            
if __name__ == "__main__":
    players = PlayerPool()
    
    print(len(players.pool))