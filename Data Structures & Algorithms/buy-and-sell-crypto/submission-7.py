class Solution:
    def maxProfit(self, prices: List[int]) -> int:   
        best = 0
        sell = 0
        buy = max(prices)
        posible_max = max(prices) - min(prices)
        for i in prices:
            if i < buy:
                best = max(best, sell - buy)
                buy = i
                sell = 0
            elif i > sell:
                sell = i
                best = max(best, sell - buy)


            if best >= posible_max:
                return best

        return best