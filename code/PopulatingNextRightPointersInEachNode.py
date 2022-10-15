"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect1(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Solution 3: DFS

        if not root: return

        stack = [root]

        while stack:

            cur = stack.pop()

            if cur.left:
                cur.left.next = cur.right

                if cur.next:
                    cur.right.next = cur.next.left

                stack.append(cur.left)
                stack.append(cur.right)

        return root

    def connect2(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Solution 2: BFS

        if not root: return

        queue = [root]

        while queue:

            cur = queue.pop(0)

            if cur.left:
                cur.left.next = cur.right

                if cur.next:
                    cur.right.next = cur.next.left

                queue.append(cur.left)
                queue.append(cur.right)

        return root

    def connect3(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Solution 1: recursive
        # Time Complexity: O(n)
        # Space Complexity:O(logn)

        if not root or not root.left:  # perfect tree之下，沒有children代表到最下一層了
            return root

        root.left.next = root.right

        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

        return root
