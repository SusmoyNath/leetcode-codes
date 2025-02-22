class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater_map = {}

        # Traverse nums2 in reverse order
        for num in reversed(nums2):
            # Maintain a decreasing stack (pop smaller elements)
            while stack and stack[-1] <= num:
                stack.pop()
            
            # If stack is not empty, top is the next greater element
            next_greater_map[num] = stack[-1] if stack else -1
            
            # Push current number onto the stack
            stack.append(num)
        
        # Build the result using nums1
        return [next_greater_map[num] for num in nums1]
