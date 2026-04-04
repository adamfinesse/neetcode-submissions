class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = defaultdict(list)

        for w in strs:
            freq = [0]*26
            for c in w:
                freq[ord(c)-ord('a')] +=1
            ana_dict[tuple(freq)].append(w)
        

        return list(ana_dict.values())