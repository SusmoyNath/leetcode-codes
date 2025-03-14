class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        x, y = 0, 0
        visited.add((x, y))  # Start at the origin

        for direction in path:
            if direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
            elif direction == 'E':
                x += 1
            elif direction == 'W':
                x -= 1

            if (x, y) in visited:
                return True  # Path crosses itself
            
            visited.add((x, y))  # Mark this coordinate as visited
        
        return False
