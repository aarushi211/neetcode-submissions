class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for i in nums:
            count[i] += 1

        sort_count = sorted(count.items(), key=lambda kv:kv[1], reverse = True)

        ans = [key for key, value in sort_count[:k]]
        
        return ans