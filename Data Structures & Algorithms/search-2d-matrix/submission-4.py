class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2

            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                new_l = 0
                new_r = len(matrix[mid]) - 1

                while new_l <= new_r:
                    new_mid = (new_l + new_r) // 2
                    if target < matrix[mid][new_mid]:
                        new_r = new_mid - 1
                    elif target > matrix[mid][new_mid]:
                        new_l = new_mid + 1
                    else: 
                        return True
                
                return False
        
        return False
