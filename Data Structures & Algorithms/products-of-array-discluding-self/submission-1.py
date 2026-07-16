class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        cnt0 = 0
        for i in nums:
            if i != 0:
                prod *= i
            else:
                cnt0 += 1

        res = []
        for i in nums:
            if cnt0 > 1:
                res.append(0)
            elif cnt0 == 1:
                if i == 0:
                    res.append(prod)
                else:
                    res.append(0)
            else:
                res.append(prod//i)

        return res