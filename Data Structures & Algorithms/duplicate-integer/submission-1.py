class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}
        for i in nums:
            if i not in duplicate:
                duplicate[i] = 1
            else:
                duplicate[i] += 1

        for value in duplicate.values():
            if value > 1:
                return True
        return False