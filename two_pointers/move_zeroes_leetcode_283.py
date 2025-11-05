from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]):
        """
        Problem analysis:
        - Given an array of integers
        - Move all 0's to the right of the array
        - Non-zero elements need to stay in their relative order

        Constraints:
        - In-place required (space constraint)
        - 1 <= nums.length <= 10^4
        - -2^31 <= nums[i] <= 2^31 - 1

        Edge-cases:
        - None

        Approach 1:
        - Instead of moving the zeroes to the left, we can also move the non-zero elements to the right
        - Use slow/fast 2 pointers approach
        - Slow pointer keeps track of first 0
        - Fast pointer looks for non-zero elements
        - Allows for one-pass

        Time & Space Complexity (respectively):
        - O(n), as we make one pass through the array
        - O(1), as we make changes in place, not changing the size of the array or declaring new data structures
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums
