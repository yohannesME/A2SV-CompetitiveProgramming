class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        events = []
        answer = [0]*n

        for booking in bookings:
            events.append([booking[0]-1, booking[2]])
            events.append([booking[1], -booking[2]])

        for event in events:
            if event[0] >= n:
                continue
            answer[event[0]] += event[1]
        
        for i in range(1,n):
            answer[i] += answer[i-1]

        return answer