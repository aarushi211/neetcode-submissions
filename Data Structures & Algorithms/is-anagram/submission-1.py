class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = []
        for letter in s:
            s1.append(letter)

        s2 = []
        for letter in t:
                s2.append(letter)

        s1.sort()
        s2.sort()
        if s1 == s2:
            return True
        return False