class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = defaultdict(list)

        for w in strs:
            freq = [0]*26
            for c in w:
                freq[ord(c)-ord('a')] +=1
            ana_dict[tuple(freq)].append(w)
        
        ans=[]
        for k in ana_dict.keys():
            ans.append(ana_dict[k])

        return ans