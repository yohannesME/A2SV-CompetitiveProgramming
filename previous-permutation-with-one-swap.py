class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        N = len(arr)

        if N == 1:
            return arr

        for i in range(N-2, -1,-1):
            if arr[i] > arr[i+1]:
                minimum = [arr[i+1], i+1]

                for j in range(i+1, N):
                    if arr[j] < arr[i] and arr[j] > minimum[0]:
                        minimum[0] = arr[j]
                        minimum[1] = j
                arr[i], arr[minimum[1]] = arr[minimum[1]], arr[i]
                break
        return arr