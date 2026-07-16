class Solution:
    def binary_search(self, low, high, nums, target):
        if low>high:
            return -1

        mid = low + (high - low)//2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.binary_search(low, mid-1, nums, target)
        else:
            return self.binary_search(mid+1, high, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)
            