# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.getVal(l1)
        num2 = self.getVal(l2)
        combined = str(num1 + num2)[::-1]
        head = ListNode(0, None)
        cur = head
        for num in combined:
            cur.next = ListNode(num, None)
            cur = cur.next
        return head.next


    def getVal(self, l: Optional[ListNode]) -> int:
        if not l:
            return 0
        stack = []
        num = ""
        cur = l
        while cur:
            stack.append(cur.val)
            cur = cur.next
        
        while stack:
            num += str(stack.pop())
        return int(num)