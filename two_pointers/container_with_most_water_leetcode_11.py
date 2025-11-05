class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Problem analysis:
        - Given int array height, for visualization we can think of an index as a wall
        - 2 indeces forming a bucket, find the pair that can hold the most water, and return said amount

        Constraints:
        - n == height.length
        - 2 <= n <= 105
        - 0 <= height[i] <= 104

        Edge-cases:
        - All walls height 0

        Approach 1:
        - Converging two pointer approach

        Time & Space Complexity (respectively):
        - O(n), as we iterate over the length of the array
        - O(1), as we do not make changes to the original array
        """
        left, right = 0, len(height) - 1

        max_water = 0
        while left < right:
            water = (min(height[left], height[right])) * (right - left)
            if water > max_water:
                max_water = water
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_water