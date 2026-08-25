class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # =========================
        # CZĘŚĆ 1: znajdź pivot
        # =========================

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left


        # =========================
        # CZĘŚĆ 2: obróć tablicę
        # =========================

        nums = nums[pivot:] + nums[:pivot]


        # =========================
        # CZĘŚĆ 3: zwykły binary search
        # =========================

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] == target:

                # =========================
                # CZĘŚĆ 4: indeks z powrotem
                # =========================

                return (mid + pivot) % len(nums)

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1