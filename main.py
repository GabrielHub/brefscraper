import obj

if __name__ == "__main__":
    players = obj.PlayerPool()
    
    print(len(players.pool), "players loaded")
    
    players.printPts()