# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Problem analysis:
        - Given a link list, I need to reverse it

        Constraints:
        - The number of nodes in the list is the range [0, 5000].
        - -5000 <= Node.val <= 5000

        Edge-cases:
        - Input is optional, can be None

        Approach 1:
        - In-place manipulation of the node list
        - Save previous node, and set current_node.next to previous

        Time & Space Complexity (respectively):
        - O(n), we need to walk through the entire node list
        - O(1), as we are manipulating the node list in place

        """
        previous = None
        while head:
            temp = head.next
            head.next = previous
            previous = head
            head = temp
        return previous
