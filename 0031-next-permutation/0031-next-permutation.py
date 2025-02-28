class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Modifies nums in-place to its next lexicographical permutation.
        """
        # Step 1: Find the first decreasing element
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            # Step 2: Find the smallest element larger than nums[i] to swap
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap elements at i and j
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the suffix to get the next permutation
        nums[i + 1:] = reversed(nums[i + 1:])
