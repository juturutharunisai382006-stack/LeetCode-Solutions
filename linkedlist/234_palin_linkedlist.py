# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        temp=head
        s=""
        while temp:
            s+=str(temp.val)
            temp=temp.next
        n=s[::-1]
        if(n==s):
            return True
        else:
            return False