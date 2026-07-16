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
                if seen[0] == s[char]:
                    #seen.pop(0)
                    continue
                res.append(best)
                seen = [s[char]]
                best = 1
        return max(res)