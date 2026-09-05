class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        valid = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for i in s:
            if i in valid.values():
                seen.append(i)
            elif seen and seen[-1] == valid[i]:
                seen.pop()
            else:
                return False

        return not seen
