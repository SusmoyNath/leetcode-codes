class Solution:
    def validIPAddress(self, queryIP):
        if self.isIPv4(queryIP):
            return "IPv4"
        if self.isIPv6(queryIP):
            return "IPv6"
        return "Neither"

    def isIPv4(self, ip):
        parts = ip.split(".")
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit() or not (0 <= int(part) <= 255):
                return False
            if part[0] == '0' and len(part) > 1:  # No leading zeros allowed
                return False
        return True

    def isIPv6(self, ip):
        parts = ip.split(":")
        if len(parts) != 8:
            return False
        hex_digits = "0123456789abcdefABCDEF"
        for part in parts:
            if not (1 <= len(part) <= 4):
                return False
            if not all(c in hex_digits for c in part):
                return False
        return True

# Example usage
solution = Solution()
print(solution.validIPAddress("172.16.254.1"))  # Output: "IPv4"
print(solution.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))  # Output: "IPv6"
print(solution.validIPAddress("256.256.256.256"))  # Output: "Neither"
