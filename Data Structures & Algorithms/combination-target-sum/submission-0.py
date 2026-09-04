class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        current = []
        def backtrack(remaining, start):
            if remaining == 0:
                return results.append(current.copy())
            if remaining < 0 :
                return
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(remaining - nums[i], i)
                current.pop()
        backtrack(target, 0)
        return results

                