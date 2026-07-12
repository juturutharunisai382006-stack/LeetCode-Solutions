class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp=head
        c=0
        while temp:
            c+=1
            temp=temp.next
        if(n==c):
            return head.next
        temp=head
        for i in range(c-n-1):
            temp=temp.next
        temp.next=temp.next.next
        return head