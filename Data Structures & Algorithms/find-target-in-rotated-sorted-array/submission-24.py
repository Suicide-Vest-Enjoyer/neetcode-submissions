class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # 1. Znajdujemy pivot
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        # 2. Wybieramy właściwą posortowaną część
        if target < nums[0]:
            left = pivot
            right = len(nums) - 1
        else:
            left = 0
            right = pivot - 1

            # Jeśli pivot == 0, cała tablica jest posortowana
            if pivot == 0:
                right = len(nums) - 1

        # 3. Binary search
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

