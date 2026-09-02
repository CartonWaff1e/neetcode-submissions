class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        lmax = [0] * len(height)
        running = 0
        for i in range(len(height)):
            lmax[i] = running
            running = max(running, height[i])

        rmax = [0] * len(height)
        running = 0
        for i in reversed(range(len(height))):
            rmax[i] = running
            running = max(running, height[i])
        for i in range(len(height)):
            total += max(0, min(lmax[i], rmax[i]) - height[i])
        return total





            

            
            



