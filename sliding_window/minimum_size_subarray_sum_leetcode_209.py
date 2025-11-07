class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Problem analysis:
        - Given int array nums and int target
        - Find smallest subarray length thats greater than target

        Constraints:
        - Assumption that array elements need to stay in same relative order
        - 1 <= target <= 109
        - 1 <= nums.length <= 105
        - 1 <= nums[i] <= 104

        Edge-cases:
        - None

        Approach 1:
        - Dynamic sliding window
        - Both edges start on 0
        - Right edge iterates over arrayt until the windowed sum is greater than target
        - Record length
        - Left edge then iterates over array, shrinking the window and looking for if a shorter length still results in sum being greater than target

        Time & Space Complexity (respectively):
        - O(n), one pass over array
        - O(1), only some constants added to memory
        """
        left = 0
        min_length = float('inf')
        w_sum = 0

        for right in range(len(nums)):
            w_sum += nums[right]

            while w_sum >= target:
                min_length = min(min_length, right - left + 1)
                w_sum -= nums[left]
                left += 1

        return 0 if min_length == float('inf') else min_length
