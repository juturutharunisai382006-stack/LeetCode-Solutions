class Solution(object):
    def addBinary(self, a, b):
        sum1=0
        l1=len(a)
        for i in range(l1):
            sum1 += int(a[i])*(2**(l1-i-1))
        sum2=0
        l2=len(b)
        for i in range(l2):
            sum2 += int(b[i])*(2**(l2-i-1))
        sum3=sum1+sum2
        s=''
        if sum3==0:
            return '0'
        while sum3>0:
            r=sum3%2
            s += str(r)
            sum3=sum3//2
        return s[::-1]