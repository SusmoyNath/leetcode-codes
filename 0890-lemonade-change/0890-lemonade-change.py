class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0  # Track $5 and $10 bills
        
        for bill in bills:
            if bill == 5:
                five += 1  # Collect $5 bill
            
            elif bill == 10:
                if five == 0:  # Can't give change
                    return False
                five -= 1
                ten += 1  # Collect $10 bill
            
            else:  # bill == 20
                if ten > 0 and five > 0:  # Prefer giving one $10 and one $5
                    ten -= 1
                    five -= 1
                elif five >= 3:  # Otherwise, give three $5 bills
                    five -= 3
                else:
                    return False  # Not enough change
        
        return True
