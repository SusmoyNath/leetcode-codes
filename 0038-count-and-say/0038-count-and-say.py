class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"  # Base case
        
        for _ in range(n - 1):  # Build up to nth sequence
            next_seq = []
            i = 0
            
            while i < len(result):
                count = 1  # Start counting the sequence
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    count += 1
                    i += 1  # Move pointer
                
                next_seq.append(str(count) + result[i])  # Append count+digit
                i += 1  # Move to next digit
            
            result = "".join(next_seq)  # Update result with the new sequence
        
        return result
