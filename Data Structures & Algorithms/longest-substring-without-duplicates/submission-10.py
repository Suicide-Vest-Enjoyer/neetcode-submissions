class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        res = [0]
        seen = []
        for char in range(len(s)):
            if s[char] not in seen:
                best += 1
                seen.append(s[char])
                res.append(best)
            else:
                res.append(best)
                if seen[0] == s[char]:
                    #best = best - seen.index(seen[0]) + 1
                    seen.append(s[char])
                    seen.pop(0)
                    continue
                seen = [s[char]]
                best = 1
        return max(res)