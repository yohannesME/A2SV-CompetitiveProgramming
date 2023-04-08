class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        N = len(image)
        M = len(image[0])
        startingColor = image[sr][sc]

        if startingColor == color:
            return image

        #direction ---up ----down --left, -right
        directions = [(1,0), (-1,0), (0,-1),(0,1)]

        def validatePath(i, j):
            return 0 <= i < N and 0 <= j < M

        def flood(sr, sc):
            for direction in directions:
                new_sr, new_sc = sr + direction[0], sc + direction[1]
                if validatePath(new_sr, new_sc):
                    if image[new_sr][new_sc] == startingColor:
                        image[sr][sc] = color
                        flood(new_sr, new_sc)
            
            image[sr][sc] = color
        
        flood(sr, sc)
        return image