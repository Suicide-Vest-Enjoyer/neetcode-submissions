from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #HashMap = {}
        #for v in nums: 
        #    HashMap[v] = HashMap.get(v, 0) + 1
        #
        #ReverseMap = defaultdict(list)
        #for key in HashMap:
        #    ReverseMap[HashMap.get(key)].append(key)

        #result = []
        #while len(result) < k:
        #    m_a_x = max(ReverseMap.keys())
        #    value = ReverseMap.get(m_a_x)
        #    for v in value:
        #        result.append(v)
        #    ReverseMap.pop(m_a_x)
        #return result

        count = {}
        freq_table = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq_table[c].append(n)

        res = []
        for i in range(len(freq_table) - 1, 0, -1):
            for n in freq_table[i]:
                res.append(n)
                if len(res) == k:
                    return res

    