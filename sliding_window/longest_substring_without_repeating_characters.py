class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Problem analysis:
        - Given string
        - Find longest substring of unique characters

        Constraints:
        - Substring can't contain duplicate chars
        - 0 <= s.length <= 5 * 104
        - s consists of English letters, digits, symbols and spaces.

        Edge-cases:
        - None

        Approach 1:
        - Dynamic sliding window
        - Right edge checks new chars against currently windowed chars
        - Left edge adjusts substring start
        - Use a set to keep track windowed chars

        Time & Space Complexity (respectively):
        - O(n), one pass over string
        - O(n), worst case the set grows to the length of n
        """
        w_chars = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in w_chars:
                w_chars.remove(s[left])
                left += 1

            w_chars.add(s[right])
            max_length = max(max_length, len(w_chars))

        return max_length
