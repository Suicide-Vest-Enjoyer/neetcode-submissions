from collections import Counter

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        answer = []
        i = 0
        while len(strs) > 0:
            answer.append([strs[0]])
            minus = 0
            for j in range(len(strs) - 1):
                #rint(f"J: {j}")
                #rint(f"I: {i}")
                #rint(f"Minus: {minus}")
                if Counter(strs[0]) == Counter(strs[j+1-minus]):
                    answer[i].append(strs[j+1-minus])
                    strs.pop(j+1-minus)
                    minus += 1
            strs.pop(0)
            i += 1

        return answer