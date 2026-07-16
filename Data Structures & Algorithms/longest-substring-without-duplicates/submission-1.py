class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alpha = set()
        max_length = 0
        j = 0
        for i in range(len(s)):
            while s[i] in alpha:
                alpha.remove(s[j])
                j += 1
            alpha.add(s[i])
            length = i-j+1
            max_length = max(max_length, length)
        return max_length