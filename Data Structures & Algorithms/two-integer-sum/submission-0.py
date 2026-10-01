class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}
        for i, num in enumerate(nums):
            neg = target-num
            if neg in seen:
                return [seen[neg],i]
            seen[num] = i
        
