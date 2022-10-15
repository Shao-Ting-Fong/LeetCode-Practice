from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # Make the gap between left right == n
        # When right moves to the end, the node on position left is the one we want to fix

        left = right = head
        for _ in range(n):
            right = right.next

        # IF there's only one element in head, return None (head.next)
        if not right:
            return head.next

        while right.next:
            left, right = left.next, right.next

        left.next = left.next.next

        return head
