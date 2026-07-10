from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        HashMap = defaultdict(list)
        for v in strs:
            c = "".join(sorted(v))
            HashMap[c].append(v)
        
    
        return list(HashMap.values())