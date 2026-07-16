class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = high

        while low <= high:
            m = (low + high)//2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p)/m)

            if totalTime <= h:
                ans = m
                high = m-1
            else:
                low = m+1
        return ans
            
