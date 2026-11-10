class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[mid][-1] < target:
                l = mid + 1
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                
               
                l1 = 0
                r1 = len(matrix[mid]) -1

                while l1 <= r1:
                    mid1 = (l1 + r1) // 2

                    if matrix[mid][mid1] < target:
                        l1 = mid1 + 1
                    elif matrix[mid][mid1] > target:
                        r1 = mid1 - 1
                    else:
                        return True            
                return False     
        return False