class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = list()
        running = 1
        for num in nums:
                prod.append(running)
                running *= num
        
        running = 1
        for i in range(len(nums) -1 , -1 , -1):
            prod[i] *= running
            running *= nums[i]
        return prod

  
            
            

            


            
        

            

        