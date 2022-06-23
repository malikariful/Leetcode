# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
        flag=0
        head=ListNode()
        cur=head
        while list1 is not None and list2 is not None:
            temp=ListNode()
            if list1.val>list2.val:
                temp.val=list2.val
                list2=list2.next
                
                
            else:
                temp.val=list1.val
                list1=list1.next
                
            cur.next=temp
            cur=cur.next
            
        while list1 is not None:
            temp=ListNode()
            temp.val=list1.val
            list1=list1.next
            cur.next=temp
            cur=cur.next
            
        while list2 is not None:
            temp=ListNode()
            temp.val=list2.val
            list2=list2.next
            cur.next=temp
            cur=cur.next
        
        head=head.next
        return head
        
