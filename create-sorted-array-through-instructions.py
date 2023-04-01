from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        sortedlist = SortedList()
        counts = defaultdict(int)
        result = 0

        for i in range(len(instructions)):
            sortedlist.add((instructions[i], i))
            position = sortedlist.index((instructions[i], i))
            result += min(position - counts[instructions[i]], i-position)
            counts[instructions[i]] += 1

        return result%(10**9 + 7)