# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        cur = head
        stack = []
        while cur:
            stack.append(cur)
            cur = cur.next
        
        cur = stack.pop()
        head = cur
        cur = head
        while stack:
            tmp = stack.pop()
            cur.next = tmp
            cur = cur.next

        cur.next = None

        return head
