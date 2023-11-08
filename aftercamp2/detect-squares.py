class DetectSquares:

    def __init__(self):
        self.coord = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.coord[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        cnt = 0
        keys = list(self.coord.keys())
        for x,y in keys:
            xdiff = abs(x-point[0])
            ydiff = abs(y-point[1])
            if xdiff == ydiff and xdiff > 0:
                cnt += self.coord[(x,y)]* self.coord[(x, point[1])]* self.coord[(point[0], y)]
        return cnt


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)