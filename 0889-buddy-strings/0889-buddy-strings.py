class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        if s == goal:
            return len(set(s)) < len(s)  # Check if a duplicate character exists
        
        # Find indices where s and goal differ
        diffs = [(a, b) for a, b in zip(s, goal) if a != b]
        
        return len(diffs) == 2 and diffs[0] == diffs[1][::-1]  # Swap check
