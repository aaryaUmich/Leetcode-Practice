class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        myset = set()
        nums1.sort()
        nums2.sort()

        len1 = len(nums1)
        len2 = len(nums2)

        nums1start = 0
        nums2start = 0

        while (nums1start < len1 and nums2start < len2):
            if nums1[nums1start] == nums2[nums2start]:
                myset.add(nums1[nums1start])
                nums1start+=1
                nums2start+=1
            
            elif nums1[nums1start] < nums2[nums2start]:
                nums1start+=1
            
            else:
                nums2start+=1
        
        final = []
        for i in myset:
            final.append(i)

        return final