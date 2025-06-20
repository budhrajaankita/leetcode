# Last updated: 6/11/2025, 10:34:34 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

       

        if head==None or head.next == None:
            return head

        odd = head
        even = head.next
        evenHead = head.next

        while even!= None and even.next != None :

            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = evenHead

        return head

        