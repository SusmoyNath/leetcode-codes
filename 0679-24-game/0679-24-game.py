from itertools import permutations

class Solution:
    def judgePoint24(self, cards):
        def backtrack(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6  # Floating-point precision check
            
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        remaining = [nums[k] for k in range(len(nums)) if k != i and k != j]
                        
                        for new_val in {nums[i] + nums[j], nums[i] - nums[j], nums[j] - nums[i], 
                                        nums[i] * nums[j]} | ({nums[i] / nums[j]} if nums[j] != 0 else set()) | \
                                        ({nums[j] / nums[i]} if nums[i] != 0 else set()):
                            if backtrack(remaining + [new_val]):
                                return True
            return False
        
        return backtrack(cards)

# â Test Cases
sol = Solution()
print(sol.judgePoint24([4,1,8,7]))  # Expected: True
print(sol.judgePoint24([1,2,1,2]))  # Expected: False
