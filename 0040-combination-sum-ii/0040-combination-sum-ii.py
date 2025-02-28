class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()  # Sort to handle duplicates

        def backtrack(start, current_combination, current_sum):
            if current_sum == target:
                result.append(list(current_combination))  # Found a valid combination
                return
            if current_sum > target:
                return  # Prune path
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:  # Skip duplicates
                    continue
                
                current_combination.append(candidates[i])  # Choose
                backtrack(i + 1, current_combination, current_sum + candidates[i])  # Move to next index
                current_combination.pop()  # Unchoose (backtrack)
        
        backtrack(0, [], 0)
        return result
