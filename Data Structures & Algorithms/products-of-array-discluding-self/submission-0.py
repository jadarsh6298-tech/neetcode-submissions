class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftp=1
        rightp=1
        results=[1] *(len(nums))
        for i in range(len(nums)):
            results[i]=leftp
            leftp*=nums[i]
        for j in range(len(nums)-1,-1,-1):
            results[j]*=rightp 
            rightp*=nums[j]
        return results