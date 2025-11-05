class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Problem analysis:
        - Given integer array nums and integer val
        - Remove occurences of val in nums
        - Order does not matter
        - First elements of nums need to be non-val's
        - Return the number of non-val integers in nums

        Constraints:
        - 0 <= nums.length <= 100
        - 0 <= nums[i] <= 50
        - 0 <= val <= 100

        Edge-cases:
        - None

        Approach 1:
        - Slow/fast two pointers
        - Fast pointer look for non-val's
        - Slow pointer keeps track of non-val's count

        Time & Space Complexity (respectively):
        - O(n), as we do a single pass
        - O(1), as we do in-place operations
        """
        left = 0
        for right in range(0, len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left
