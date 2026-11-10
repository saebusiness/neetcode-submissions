class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while l <= r:
            
            m = (l + r) // 2

            
            if matrix[m][0] == target:
                return True

            elif matrix[m][-1] < target:
                l = m + 1
                
            elif matrix[m][0] > target:
                r = m - 1

            else:
                new_l = 0
                new_r = len(matrix[m]) - 1

                while new_l <= new_r:
                    new_mid = (new_l + new_r) // 2
                    
                    

                    if matrix[m][new_mid] == target:
                        return True
                    elif matrix[m][new_mid] < target:
                        new_l = new_mid + 1
                    else:
                        new_r = new_mid - 1
                return False
        
        return False