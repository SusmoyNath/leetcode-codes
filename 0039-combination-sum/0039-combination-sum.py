class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        
        def backtrack(start, current_combination, current_sum):
            if current_sum == target:
                result.append(list(current_combination))  # Found a valid combination
                return
            if current_sum > target:
                return  # Prune path
            
            for i in range(start, len(candidates)):  # Allow reuse of same number
                current_combination.append(candidates[i])  # Choose
                backtrack(i, current_combination, current_sum + candidates[i])  # Explore
                current_combination.pop()  # Unchoose (backtrack)
        
        backtrack(0, [], 0)
        return result
