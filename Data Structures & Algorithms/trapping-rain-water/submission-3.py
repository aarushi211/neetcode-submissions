class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = height[0]
        rightMax = height[n-1]
        l, r = 0, n-1
        res = 0

        while l<r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]

            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res
