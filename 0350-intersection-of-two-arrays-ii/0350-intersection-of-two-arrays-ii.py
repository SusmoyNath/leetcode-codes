from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        count1 = Counter(nums1)  # Count occurrences in nums1
        count2 = Counter(nums2)  # Count occurrences in nums2
        result = []

        # Find common elements and their minimum frequency
        for num in count1:
            if num in count2:
                result.extend([num] * min(count1[num], count2[num]))

        return result
