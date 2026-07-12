class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        num3=[]
        num3=nums1+nums2
        num3.sort()
        l=len(num3)
        if(l%2!=0):
            med=int(l/2)
            midterm=num3[med]
            return midterm
        else:
            med=l/2
            midterm=float(num3[med]+num3[med-1])/2
            return midterm

        