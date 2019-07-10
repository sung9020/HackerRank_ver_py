class Solution:
    def maxProfit(self, prices):
        result = 0
        current_max = 0
        current = 0
        i = 0
        while i < len(prices):
            current = prices[i]
            for j in range(i + 1, len(prices)):
                if prices[j] >= current:
                    if current_max < (prices[j] - current):
                        current_max = (prices[j] - current)
                        i = j - 1
                    else:
                        i = j - 1
                        break
                else:
                    i = j - 1
                    break
            result += current_max
            current_max = 0
            i += 1
        return result