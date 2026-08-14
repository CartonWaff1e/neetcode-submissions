class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = list()
        running = 1
        for num in nums:
                prod.append(running)
                running *= num
        
        running = 1
        for i in reversed(range(len(nums))):
            prod[i] *= running
            running *= nums[i]
        return prod

  
            
            

            


            
        

            

        