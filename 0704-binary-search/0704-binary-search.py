class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lt = 0
        rt = n-1
        while lt <= rt:
            key = (lt + rt)//2
            if nums[key] == target:
                return key
            
            elif nums[key] < target:
                lt += 1
            
            else:
                rt -= 1
        
        return -1
    