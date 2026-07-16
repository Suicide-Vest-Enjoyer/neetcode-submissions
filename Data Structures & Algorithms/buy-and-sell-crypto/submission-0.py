class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #if prices.sort() == prices.reverse():
            #return 0
        
        best = 0
        sell = 0
        buy = max(prices)
        for i in prices:
            if i > sell:
                sell = i
                best = max(best, sell - buy)
            if i < buy:
                best = max(best, sell - buy)
                buy = i
                sell = 0
            print(f"Sell | {sell}")
            print(f"Buy | {buy}")


        return best