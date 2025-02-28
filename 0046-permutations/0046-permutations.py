class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(path, used):
            if len(path) == len(nums):  # Base case: Full permutation found
                result.append(path[:])
                return
            
            for num in nums:
                if num not in used:  # Ensure uniqueness
                    path.append(num)
                    used.add(num)
                    backtrack(path, used)
                    path.pop()  # Undo choice
                    used.remove(num)
        
        backtrack([], set())
        return result
