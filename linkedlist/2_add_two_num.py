class Solution(object):
    def addTwoNumbers(self, l1, l2):
        temp1=l1
        temp2=l2
        st1=''
        st2=''
        while temp1:
            st1+=str(temp1.val)
            temp1=temp1.next
        while temp2:
            st2+=str(temp2.val)
            temp2=temp2.next
        sum=int(st1[::-1])+int(st2[::-1])
        if sum==0:
            return ListNode(0)     
        r=sum%10
        self.head=ListNode(r)
        temp=self.head
        sum=sum//10
        while sum>0:
            r=sum%10
            new=ListNode(r)
            temp.next=new
            sum=sum//10
            temp=temp.next
        return self.head