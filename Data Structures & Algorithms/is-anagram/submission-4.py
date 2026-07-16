class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        s = list(s)
        t = list(t)

        for i in s:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1

        for i in t:
            if i not in dict2:
                dict2[i] = 1
            else:
                dict2[i] += 1

        return dict1 == dict2
        