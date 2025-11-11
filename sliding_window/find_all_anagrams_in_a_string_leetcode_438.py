class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Problem analysis:
        - Given 2 strings, s and p
        - I need to find all anagrams of p, inside of s and return the starting indeces

        Constraints:
        - 1 <= s.length, p.length <= 3 * 104
        - s and p consist of lowercase English letters.

        Edge-cases:
        - No anagrams found -> probably just return an empty list
        - s is smaller than p
        - s is the same size as p

        Approach 1:
        - Constant sliding window
        - Length of window is determined by the length of string p
        - Slide the window through s, checking the current windowed chars and checking them against p
        - If match add to results list

        Time & Space Complexity (respectively):
        - O(n), one pass over array
        - O(n), extra list to keep track of indeces that could grow with input
        """
        s_len = len(s)
        p_len = len(p)
        indeces = []

        # Check edge case
        if s_len < p_len:
            return indeces

        # Build dicts containing char counters for each string
        w_counter = {}
        p_counter = {}
        for i in range(len(p)):
            s_char = s[i]
            p_char = p[i]
            w_counter[s_char] = w_counter.get(s_char, 0) + 1
            p_counter[p_char] = p_counter.get(p_char, 0) + 1

        # Need to check starting window seperately
        if w_counter == p_counter:
            indeces.append(0)

        for right in range(p_len, s_len):
            left = right - p_len

            # Slide window
            w_counter[s[left]] -= 1
            if w_counter[s[left]] == 0:
                del w_counter[s[left]]
            w_counter[s[right]] = w_counter.get(s[right], 0) + 1

            if w_counter == p_counter:
                indeces.append(left + 1)

        return indeces
