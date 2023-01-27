class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        #players matched with trainers
        match = 0
        
        #size of the player and trainers
        playersize = len(players)
        trainersize = len(trainers)
        
        #sort the players and trainers reverse
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        
        #traverse through the trainer and the players
        trainerptr = 0
        playerptr = 0
        
        while playerptr < playersize and trainerptr < trainersize:
            #move player until we reach a player we can train
            while playerptr < playersize and players[playerptr] > trainers[trainerptr]:
                playerptr += 1
            
            #add the found player and move to check for the next player and trainer
            if playerptr < playersize:
                match += 1
                trainerptr += 1
                playerptr += 1
        
        return match
        