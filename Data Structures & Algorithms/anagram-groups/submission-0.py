class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            s_word = ''.join(sorted(s))
            anagram_map[s_word].append(s)

        return list(anagram_map.values())