from collections import Counter

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        HashMap = {}
        answer = []
        for v in strs:
            counter = Counter(v)
            c = tuple(sorted(counter.items()))
            if c in HashMap:
                HashMap.get(c).append(v)
            else:
                HashMap[c] = [v]

        for key in HashMap:
            value = HashMap.get(key)
            answer.append(value)
        return answer