class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Problem analysis:
        - Given int array nums and int k
        - Find a sub-array with the highest average value

        Constraints:
        - n == nums.length
        - 1 <= k <= n <= 105
        - -104 <= nums[i] <= 104

        Edge-cases:
        - None

        Approach 1:
        - Sliding fixed window of length k
        - Starting window is first k elements of nums
        - Keep adding from the right edge while removing from the left edge to move the window
        - Keep track of the max sum value of the window and divide by k before returning

        Time & Space Complexity (respectively):
        - O(n), one pass over nums length
        - O(1), only some constraints added to memory
        """
        current_sum = sum(nums[:k])
        max_sum = current_sum

        for right in range(k, len(nums)):
            current_sum += nums[right] - nums[right - k]
            max_sum = max(max_sum, current_sum)

        return max_sum / k
