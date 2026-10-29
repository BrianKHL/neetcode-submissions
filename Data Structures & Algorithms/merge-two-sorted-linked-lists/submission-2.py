# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        extra = ListNode()
        tail = extra

        while(list1 != None and list2 != None):
            if (list1.val < list2.val):
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            #Don't forget this!!!    
            tail = tail.next
            
        if(list1 != None):
            tail.next = list1
        else:
            tail.next = list2

        return extra.next