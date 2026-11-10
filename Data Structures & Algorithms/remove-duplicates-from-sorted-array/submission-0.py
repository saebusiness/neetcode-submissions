class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
            
        back = 0
        front = 1
        while front < len(nums):
            if nums[back] == nums[front]:
                nums.pop(back)
            else:
                back += 1
                front += 1
            
        return len(nums)
        