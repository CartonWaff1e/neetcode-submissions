class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = list()
        running = 1
        for num in nums:
                left_prod.append(running)
                running *= num
        
        running = 1
        for i in range(len(nums) -1 , -1 , -1):
            left_prod[i] *= running
            running *= nums[i]
        return left_prod

  
            
            

            


            
        

            

        