class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        htable = set()
        for num in nums:
            if num in htable:
                return True
            htable.add(num)
        return False

         