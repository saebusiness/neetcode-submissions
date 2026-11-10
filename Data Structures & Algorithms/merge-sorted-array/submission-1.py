class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        pnums1 = m - 1
        pnums2 = n - 1


        for i in range(m+n-1, -1, -1):

            if pnums2 < 0 or (pnums1 >= 0 and nums1[pnums1] > nums2[pnums2]):
                nums1[i] = nums1[pnums1]
                pnums1 -= 1
            else:
                nums1[i] = nums2[pnums2]
                pnums2 -= 1
            
            
                


        """
        Do not return anything, modify nums1 in-place instead.
        """
        