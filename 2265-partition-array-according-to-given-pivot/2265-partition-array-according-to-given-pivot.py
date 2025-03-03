class Solution:
    def pivotArray(self, nums, pivot):
        less, equal, greater = [], [], []

        # Partition elements into three lists
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)

        # Concatenate the three lists while preserving order
        return less + equal + greater
