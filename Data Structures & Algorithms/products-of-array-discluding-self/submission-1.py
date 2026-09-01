class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = 1
        r = 1
        results = [1] * len(nums)
        for i in range(len(nums)) :
            results[i] = l
            l *= nums[i]
        for j in range(len(nums)-1, -1 , -1) :
            results[j] *= r
            r *= nums[j]
        return results