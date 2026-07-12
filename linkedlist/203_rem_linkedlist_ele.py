# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        temp=head
        prev=None
        while temp:
            if(temp.val==val and temp is head):
                head=temp.next
                temp=head
            elif(temp.val==val):
                prev.next=temp.next
                temp=temp.next
            else:
                prev=temp
                temp=temp.next
        return head