class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for i in range(len(s)):
            alpha = set()
            length = 0
            for j in range(i, len(s)):
                if s[j] in alpha:
                    break
                alpha.add(s[j])
                length += 1
            max_length = max(length, max_length)
        return max_length