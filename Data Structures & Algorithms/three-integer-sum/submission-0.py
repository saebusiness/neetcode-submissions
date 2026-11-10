class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 2:
            return []


        """
        def partition(arr,low,high):
            pivot = arr[low]
            i = -1
            j = len(arr) + 1

            while True:

                i += 1
                while arr[i] < pivot:
                    i += 1
                
                j -= 1
                while arr[j] > pivot:
                    j -= 1
                
                if i => j:
                    return j
                
                arr[i], arr[j] = arr[j], arr[i]

        def quicksort(arr, low, high):

            if low < high:
                p = partition(arr, low, high)

                quicksort(arr, low, p)
                quicksort(arr, p + 1, high)
        
        quicksort(nums)
        """
        nums.sort()
        
        return_arr = []

        for i in range(len(nums) - 2):
            front = i + 1
            back = len(nums) - 1
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            
            while front < back:
                if nums[front] + nums[back] + nums[i] > 0:                    
                    back -= 1
                    
                elif nums[front] + nums[back] + nums [i] < 0:                   
                    front += 1
                
                else:
                    yay = [nums[front] , nums[back] ,nums[i]]
                    return_arr.append(yay)

                    while front < back and nums[front] == nums[front + 1]:
                        front += 1
                    while front < back and nums[back] == nums[back - 1]:
                        back -= 1

                    front += 1
                    back -= 1
                    
        return return_arr
            
            
            

                


            
            
            
            

        



        