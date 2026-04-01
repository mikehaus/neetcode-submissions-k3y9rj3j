# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = "", ""
        n1, n2 = l1, l2

        while l1:
            cur = l1.val
            s1 += str(cur)
            l1 = l1.next
        while l2:
            cur = l2.val
            s2 += str(cur)
            l2 = l2.next
        val = str(int(s1[::-1]) + int(s2[::-1]))
        head = ListNode(None)
        cur = head
        for char in val[::-1]:
            cur.next = ListNode(int(char))
            cur = cur.next
        return head.next
        