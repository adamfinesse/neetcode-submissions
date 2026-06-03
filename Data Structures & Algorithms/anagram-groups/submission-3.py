class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            alpha_arr = [0]*26
            for c in s:
                alpha_arr[ord(c)-ord('a')] +=1
            anagram_map[tuple(alpha_arr)].append(s)
        
        res = []
        for l in anagram_map.values():
            res.append(l)
        return res