class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        final_arr = []

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                    continue

            for j in range(i + 1, len(nums) - 2):

                l = j + 1
                r = len(nums) - 1

                
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                while l < r:
                
                    
                    current_sum = nums[i] + nums[j] + nums[l] + nums[r]

                    if current_sum < target:
                        l += 1
                    elif current_sum > target:
                        r -= 1
                    else:

                        arr = [nums[i],nums[j],nums[l],nums[r]]
                        final_arr.append(arr)
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        
                        l += 1
                        r -= 1
                    
        return final_arr


            