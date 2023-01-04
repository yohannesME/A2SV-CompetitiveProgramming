class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        #declare the output
        output = []
        
        rowsize = 8
        columnsize = 8
        
        #all the queens that can attack
        attackers = defaultdict(list)
        
        #get all potential attackers
        for row, column in queens:
            if row == king[0]:
                attackers['row'].append(column)
            elif column == king[1]:
                attackers['column'].append(row)
            elif row - column == king[0]-king[1]:
                attackers['diagonal'].append(row)
            elif (row-king[0] + column-king[1] == 0):
                attackers['diagonalLeft'].append(row)
        
        #find the nearest from both the right and left
        bigleft = -1
        smallright = 8
        #all column in the same row as the king
        for column in attackers['row']:
            #check if the column is by the right or left
            if column > king[1]:
                smallright = min(smallright, column)
            else:
                bigleft = max(bigleft, column)
         
        #add the one on the right
        if smallright != 8:
            output.append([king[0], smallright])
         
        #add the one on the left
        if bigleft != -1:
            output.append([king[0],bigleft])

        #reintialize to check for the column now
        bigleft = -1
        smallright = 8                
                
        #all row in the same column as the king
        for row in attackers['column']:
            #check if the column is by the right or left
            if row > king[0]:
                smallright = min(smallright, row)
            else:
                bigleft = max(bigleft, row)
 
        #add the one on the right
        if smallright != 8:
            output.append([smallright,king[1]])
         
        #add the one on the left
        if bigleft != -1:
            output.append([bigleft,king[1]])
            
        #reintialize to check for the column now
        bigleft = -1
        smallright = 8        

        
        #all x coordinalte in the same diagonal axis as the king
        for diagonal in attackers['diagonal']:
            #check if the diagon is by the right or left
            if diagonal > king[0]:
                smallright = min(smallright, diagonal)
            else:
                bigleft = max(bigleft, diagonal)
        
 
        #add the one on the right
        if smallright != 8:
            #find the amount of change to add to the column
            change = smallright - king[0]
            output.append([smallright,king[1]+change])
         
        #add the one on the left
        if bigleft != -1:
            #find the amount of change to decrease from the column
            change = king[0] - bigleft
            output.append([bigleft,king[1]-change])
            
        #reintialize to check for the column now
        bigleft = -1
        smallright = 8        
  
        #all x coordinalte in the same diagonal axis as the king
        for diagonal in attackers['diagonalLeft']:
            #check if the diagon is by the right or left
            if diagonal > king[0]:
                smallright = min(smallright, diagonal)
            else:
                bigleft = max(bigleft, diagonal)
        
 
        #add the one on the right
        if smallright != 8:
            #find the amount of change to add to the column
            change = smallright - king[0]
            output.append([smallright,king[1]-change])
         
        #add the one on the left
        if bigleft != -1:
            #find the amount of change to decrease from the column
            change = king[0] - bigleft
            output.append([bigleft,king[1]+change])
        
        return output
                