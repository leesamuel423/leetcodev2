# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l1 = curr_l1 = ListNode(0)
        l2 = curr_l2 = ListNode(0)

        curr = head

        while curr:
            if curr.val < x:
                curr_l1.next = curr
                curr_l1 = curr_l1.next
            else:
                curr_l2.next = curr
                curr_l2 = curr_l2.next
            curr = curr.next

        curr_l2.next = None
        curr_l1.next = l2.next

        return l1.next




"""

what if we break into two lists:
l1 = values less than x
l2 =  vallues equal to or greater than x

iterate through LL
    if less than x
        add to l1
    if equal to or greater than x:
        add to l2

combine two LLs

"""

            
            
        