class Solution:
    def knightDialer(self, n: int) -> int:
        adjList = {
            1: [6,8],
            2: [9,7],
            3: [8,4],
            4: [3,9, 0],
            5: [],
            6: [1,7,0],
            7: [2,6],
            8: [1,3],
            9: [4,2],
            0: [6, 4]
        }
        memo = {}

        def search(node, length):
            if length == 1:
                return 1
            state = (node, length)

            if state in memo:
                return memo[state]

            ans = 0
            for i in adjList[node]:
                ans += search(i, length-1)
            
            memo[state] = ans
            return ans
        
        answer = 0
        for i in adjList:
            answer += search(i, n)
        
        return answer % (10**9 + 7)