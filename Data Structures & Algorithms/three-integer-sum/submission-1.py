class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)
        triplets = list()
        for num in range(len(snums)):
            negative = 0 - snums[num]
            left = num + 1
            right = len(snums)-1
            if num > 0 and snums[num] == snums[num-1]: continue
            while left < right:
                if snums[left] + snums[right] == negative:
                    triplets.append([snums[left], snums[right], snums[num]])
                    left += 1
                    right -= 1
                    while left < right and snums[left] == snums[left-1]:
                        left +=1

                elif snums[left] + snums[right] < negative:
                    left += 1
                else:
                    right -= 1

        return triplets



            

        

