from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Count student preferences
        count0 = students.count(0)
        count1 = students.count(1)

        # Process sandwiches
        for s in sandwiches:
            if s == 0 and count0 > 0:
                count0 -= 1
            elif s == 1 and count1 > 0:
                count1 -= 1
            else:
                # No students left who want the top sandwich
                return count0 + count1
        
        return 0  # All students are served
