class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = defaultdict(list)

        for w in strs:
            ana_dict[tuple(sorted(w))].append(w)
        
        ans=[]
        for k in ana_dict.keys():
            ans.append(ana_dict[k])

        return ans