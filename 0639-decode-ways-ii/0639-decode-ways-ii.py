class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7

        # Edge case
        if not s:
            return 0

        # Rolling DP variables
        prev2, prev1 = 1, 0  # dp[-1] = 1, dp[0] will be calculated next

        # First character decoding
        if s[0] == '*':
            prev1 = 9  # '*' can be 1-9
        elif s[0] == '0':
            prev1 = 0  # Invalid case
        else:
            prev1 = 1  # Single valid digit

        # Iterate over the string
        for i in range(1, len(s)):
            curr = 0  # dp[i]
            
            # Case 1: Single character decoding
            if s[i] == '*':
                curr += 9 * prev1  # '*' can be '1' to '9'
            elif s[i] != '0':  # Normal digit
                curr += prev1

            # Case 2: Two-character decoding
            if s[i - 1] == '*' and s[i] == '*':
                curr += 15 * prev2  # "**" â "11-19" (9 cases) + "21-26" (6 cases)
            elif s[i - 1] == '*':
                if '0' <= s[i] <= '6':  # "*0" to "*6" â "10-16", "20-26" (2 cases)
                    curr += 2 * prev2
                else:  # "*7" to "*9" â "17-19" (only 1 case)
                    curr += prev2
            elif s[i] == '*':
                if s[i - 1] == '1':  # "1*": Can be "11-19" (9 cases)
                    curr += 9 * prev2
                elif s[i - 1] == '2':  # "2*": Can be "21-26" (6 cases)
                    curr += 6 * prev2
            else:
                two_digit = int(s[i - 1:i + 1])
                if 10 <= two_digit <= 26:  # Valid two-digit number
                    curr += prev2

            # Apply modulo constraint
            curr %= MOD

            # Shift DP variables forward
            prev2, prev1 = prev1, curr

        return prev1
