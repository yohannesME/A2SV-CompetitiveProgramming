class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        #diagonal elements
        output = []
        #           down dig, up dig, to down, to right
        [downdig, updig, down, right] = [(1,-1), (-1,1), (1,0), (0,1)  ]
        
        x = len(mat)
        y = len(mat[0])
        
        i = 0
        j = 0
        
        up = True
        
        #breaks when it reaches the last index
        while not ( ( x-1) == i and (y-1) == j):
            
            #input the element traversing by diagonal
            output.append(mat[i][j])
            
            #move up the diagonal side
            if up:
                #if done traversing up switch and start traversing down
                if not self.outofbound(i+updig[0], j+updig[1],x,y):
                    i += updig[0]
                    j += updig[1]
                else:
                    up = False
                    #move right or down depending on the current position
                    if not self.outofbound(i+right[0], j+right[1],x,y):
                        i += right[0]
                        j += right[1]
                    else:
                        i += down[0]
                        j += down[1]
            #move down the diagonal side
            else:
                #if done traversing down switch and traverse up
                if not self.outofbound(i+downdig[0], j+downdig[1],x,y):
                    i += downdig[0]
                    j += downdig[1]
                else:
                    up = True
                    #move down or right depending on the current position
                    if not self.outofbound(i+down[0], j+down[1],x,y):
                        i += down[0]
                        j += down[1]
                    else:
                        i += right[0]
                        j += right[1]               

        #add the last element that we used to break out of the while loop
        output.append(mat[i][j])
        
        return output
        
    #check if the move makes the index out of bound
    def outofbound(self,i,j, x,y):
        return i >= x or i < 0  or j >= y or j < 0
