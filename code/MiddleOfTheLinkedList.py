from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def middleNode1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Solution 1: Brutal Force
        # Time Complexity:O(n)
        # Space Complexity: O(n)

        LinkedList = []
        while head:
            LinkedList.append(head)
            head = head.next

        return LinkedList[len(LinkedList)//2]

    def middleNode2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Solution 2:Two Pointers: Fast and Slow
        # Fast go two steps each, slow go one step
        # When fast finish, slow pointer is at the midpoint

        # Time Complexity:O(n)
        # Space Complexity:O(1)

        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
