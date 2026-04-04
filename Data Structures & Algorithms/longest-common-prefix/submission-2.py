class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.num_children=0
        self.end_of_word = False

def insert(root,word):
    curr = root
    for c in word:
        pos = ord(c) - ord('a')
        if curr.children[pos] == None:
            curr.children[pos] = TrieNode()
            curr.num_children +=1
            
        curr = curr.children[pos]
    curr.end_of_word = True

def search_lcp(root,word):
    lcp = ""
    for c in word:
        pos = ord(c) - ord('a')
        if root.children[pos] == None or root.end_of_word or root.num_children >1:
            return lcp
        root = root.children[pos]
        lcp += c
    return lcp

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = TrieNode()

        for w in strs:
            insert(root,w)

        return search_lcp(root,strs[0])




