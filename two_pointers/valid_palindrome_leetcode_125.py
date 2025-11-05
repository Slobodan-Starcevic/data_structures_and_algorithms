class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Problem analysis:
        - Given a potential palindrome
        - Check if it is one
        - Return bool

        Constraints:
        - 1 <= s.length <= 2 * 105

        Edge-cases:
        - non-alphanumeric characters included

        Approach 1:
        - Converging two pointer
        - The moment the pointers are not the same, we return False

        Time & Space Complexity (respectively):
        - O(n), single pass over string
        - O(1), as the input does not change
        """
        s = ''.join(filter(str.isalnum, s)).lower()
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1
        return True