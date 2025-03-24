from typing import List

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        
        # Precompute prefix sums of skill.
        # prefix[i] = sum_{r=0}^{i-1} skill[r], with prefix[0] = 0.
        prefix = [0] * (n + 1)
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + skill[i-1]
        
        # Compute finish times for potion 0.
        prev_finish = [0] * n
        prev_finish[0] = 0 + skill[0] * mana[0]
        for i in range(1, n):
            prev_finish[i] = prev_finish[i-1] + skill[i] * mana[0]
        
        # Process potions 1 through m-1.
        for j in range(1, m):
            # Determine the minimum feasible start time P for potion j.
            # Constraint from wizard 0: P >= prev_finish[0]
            P = prev_finish[0]
            for i in range(1, n):
                # Constraint from wizard i:
                # P >= prev_finish[i] - (sum of skill[0..i-1]) * mana[j]
                P = max(P, prev_finish[i] - prefix[i] * mana[j])
            
            # Now compute finish times for potion j.
            current_finish = [0] * n
            current_finish[0] = P + skill[0] * mana[j]
            for i in range(1, n):
                current_finish[i] = current_finish[i-1] + skill[i] * mana[j]
            
            prev_finish = current_finish
        
        return prev_finish[-1]
