from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Problem analysis:
        - Given integer array, sorted ascending
        - Remove duplicates in-place
        - Each element must be unique while keeping relative order
        - Return count of unique numbers
        - Array should start with the unique numbers, sorted
        - Beyond unique elements can be ignored

        Constraints:
        - In-place removal (space constraint)
        - 1 <= nums.length <= 3 * 10^4
        - -100 <= nums[i] <= 100
        - nums is sorted in ascending order

        Edge-cases:
        - None

        Approach 1:
        - Slow/fast two pointers approach
        - Fast pointer looks iterates through array
        - Slow pointer keeps track of found unique elements
        - Start at index 1 and keep comparing with index left-1

        Time & Space Complexity (respectively):
        - O(n), as we are doing one pass through the array
        - O(1), as we are doing in-place changes, not changing the length of nums
        """
        left = 1
        for right in range(1, len(nums)):
            if nums[right] != nums[left - 1]:
                nums[left] = nums[right]
                left += 1
        return left
