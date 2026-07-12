# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        c=0
        temp=head
        while temp:
            c+=1
            temp=temp.next
        mid=(c//2)
        temp=head
        for i in range(mid):
            head=temp.next
            temp=temp.next
        return head