# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        temp1=list1
        temp2=list2
        head=ListNode(0)
        t=head
        if temp1 is None:
            return list2
        if temp2 is None:
            return list1
        while temp1 and temp2:
            if(temp1.val<=temp2.val):
                t.next=ListNode(temp1.val)
                t=t.next
                temp1=temp1.next
            else:
                t.next=ListNode(temp2.val)
                t=t.next
                temp2=temp2.next
        while temp1:
            t.next=ListNode(temp1.val)
            t=t.next
            temp1=temp1.next
        while temp2:
            t.next=ListNode(temp2.val)
            t=t.next
            temp2=temp2.next
        return head.next

                