from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        HashMap = {}
        for v in nums: 
            HashMap[v] = HashMap.get(v, 0) + 1
        
        
        ReverseMap = defaultdict(list)
        for key in HashMap:
            ReverseMap[HashMap.get(key)].append(key)

        print(ReverseMap)
        result = []
        while len(result) < k:
            m_a_x = max(ReverseMap.keys())
            value = ReverseMap.get(m_a_x)
            for v in value:
                result.append(v)
            ReverseMap.pop(m_a_x)
        return result