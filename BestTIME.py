class Solution:
    def maxProfit(self, prices):
        result = 0
        current_max = 0
        current = 0
        for i in range(len(prices)):
            current = prices[i]
            for j in range(i + 1, len(prices)):
                if prices[j] < current:
                    break;
                else:
                    current_max = max(current_max, (prices[j] - prices[i]))
            result += current_max
            current_max = 0
        return max