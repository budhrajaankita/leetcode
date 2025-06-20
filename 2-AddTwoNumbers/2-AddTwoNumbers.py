# Last updated: 6/11/2025, 10:35:17 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
           val1 = l1.val if l1 else 0
           val2 = l2.val if l2 else 0

           summ = val1 + val2 + carry

           carry = summ // 10

           curr_val = summ % 10

           curr.next = ListNode(curr_val)


           curr = curr.next
           l1 = l1.next if l1 else None
           l2 = l2.next if l2 else None

        return dummy.next

        
        # print(n1)