class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        requestHandled = 0
        N = len(requests)

        #[out, input] for each building is kept here and below check if input == output
        requestTrack = [[0]*2 for _ in range(n)]

        #validate if all request are optimal if not return 0 as not yet if not sum of all request made until this point
        def validRequest():
            requestCount = 0
            for request in requestTrack:
                requestCount += request[0]
                if request[0] != request[1]:
                    break
            else:
                return requestCount
            
            return 0

        def backtrack(index):
            nonlocal N, requestHandled
            #check if current handled request satisfies and update request handled
            requestHandled = max(validRequest(), requestHandled)

            #[from -> out, to -> input]
            for i in range(index, N):
                requestTrack[requests[i][0]][0] += 1
                requestTrack[requests[i][1]][1] += 1
                backtrack(i+1)
                requestTrack[requests[i][0]][0] -= 1
                requestTrack[requests[i][1]][1] -= 1

        backtrack(0)
        return requestHandled