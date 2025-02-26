class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        has_lower = has_upper = has_digit = False
        replace_count = 0
        one_mod = two_mod = 0  # Track repeat groups of length % 3 == 1 or 2
        
        i = 0
        while i < n:
            if password[i].islower():
                has_lower = True
            if password[i].isupper():
                has_upper = True
            if password[i].isdigit():
                has_digit = True

            j = i
            while i < n and password[i] == password[j]:
                i += 1  # Move to next character
            
            # Found a sequence of length >= 3
            length = i - j
            if length >= 3:
                replace_count += length // 3  # Number of replacements needed
                if length % 3 == 0:
                    one_mod += 1
                elif length % 3 == 1:
                    two_mod += 1

        missing_types = 3 - sum([has_lower, has_upper, has_digit])

        # **Case 1: If length < 6, we need insertions**
        if n < 6:
            return max(6 - n, missing_types)

        # **Case 2: If length is between 6 and 20, just replace**
        elif n <= 20:
            return max(replace_count, missing_types)

        # **Case 3: If length > 20, we need deletions**
        else:
            excess = n - 20
            delete_count = excess
            
            # Reduce replacements using deletions
            replace_count -= min(excess, one_mod)  # Remove 1 character from %3 == 0 groups
            replace_count -= min(max(excess - one_mod, 0), two_mod * 2) // 2  # Remove 2 characters from %3 == 1 groups
            replace_count -= max(excess - one_mod - 2 * two_mod, 0) // 3  # Remove 3 characters from %3 == 2 groups
            
            return excess + max(replace_count, missing_types)
