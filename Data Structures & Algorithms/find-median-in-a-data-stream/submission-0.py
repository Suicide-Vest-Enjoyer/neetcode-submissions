
class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        left = 0
        right = len(self.arr)

        while left < right:
            mid = (left + right) // 2

            if self.arr[mid] < num:
                left = mid + 1
            else:
                right = mid

        self.arr.insert(left, num)

    def findMedian(self) -> float:
        n = len(self.arr)

        if n % 2 == 1:
            return self.arr[n // 2]

        return (self.arr[n // 2 - 1] + self.arr[n // 2]) / 2
