class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        from collections import Counter
        need = Counter(t)
        required = len(need)         

        window = {}
        formed = 0

        left = 0
        best_len = float('inf')
        best_left = 0

        for right, c in enumerate(s):
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                formed += 1
                
            while formed == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left

                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                left += 1

        return "" if best_len == float('inf') else s[best_left:best_left + best_len]