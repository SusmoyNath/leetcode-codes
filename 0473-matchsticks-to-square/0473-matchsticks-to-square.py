class Solution(object):
    def makesquare(self, matchsticks):
        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False
        
        target = total_length // 4
        matchsticks.sort(reverse=True)  # Sorting in descending order helps prune invalid cases earlier
        sides = [0] * 4  # Represents the four sides of the square
        
        def backtrack(index):
            if index == len(matchsticks):
                return all(side == target for side in sides)
            
            for i in range(4):
                if sides[i] + matchsticks[index] <= target:
                    sides[i] += matchsticks[index]
                    if backtrack(index + 1):
                        return True
                    sides[i] -= matchsticks[index]
                
                if sides[i] == 0:  # If the first stick doesnât fit, there's no need to try the others
                    break
            
            return False
        
        return backtrack(0)
