class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if valueDiff < 0:
            return False  # Absolute difference cannot be negative
        
        bucket_size = valueDiff + 1  # Define bucket width
        buckets = {}  # Dictionary to store bucket mappings

        for i, num in enumerate(nums):
            bucket_id = num // bucket_size  # Find the bucket for current num

            # Case 1: If bucket already contains a number, return True
            if bucket_id in buckets:
                return True
            
            # Case 2: Check adjacent buckets for a close enough value
            if (bucket_id - 1 in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff):
                return True
            if (bucket_id + 1 in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff):
                return True

            # Add current number to its bucket
            buckets[bucket_id] = num

            # Maintain window of size indexDiff (remove out-of-range numbers)
            if i >= indexDiff:
                old_bucket_id = nums[i - indexDiff] // bucket_size
                del buckets[old_bucket_id]

        return False
