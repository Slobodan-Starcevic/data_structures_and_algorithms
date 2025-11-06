class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Problem analysis:
        - Given int array of prices
        - Pick one day to buy and one day to sell
        - If no profit return 0

        Constraints:
        - 1 <= prices.length <= 105
        - 0 <= prices[i] <= 104

        Edge-cases:
        - If no profit can be made, return 0

        Approach 1:
        - Fast/slow two pointers
        - Fast checks for lowest price and higher prices
        - Slow keeps track of lowest price

        Time & Space Complexity (respectively):
        - O(n), one pass over array
        - O(1), only constants added
        """
        left = 0
        max_profit = 0

        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
                continue
            current_profit = prices[right] - prices[left]
            max_profit = max(max_profit, current_profit)
        return max_profit
