class Solution(object):
    def searchInsert(self, nums, target):
        s=0
        e=len(nums)-1
        while(s<=e):
            mid=(s+e)//2
            if(nums[mid]<target):
                s=mid+1
            elif(nums[mid]>target):
                e=mid-1
            else:
                return mid
        return s