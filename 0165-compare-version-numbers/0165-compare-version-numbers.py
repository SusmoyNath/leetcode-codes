class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))

        max_len = max(len(v1), len(v2))
        v1.extend([0] * (max_len - len(v1)))
        v2.extend([0] * (max_len - len(v2)))

        for i in range(max_len):
            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1
        return 0

# Test cases
sol = Solution()
print(sol.compareVersion("1.2", "1.10"))     # Output: -1
print(sol.compareVersion("1.01", "1.001"))   # Output: 0
print(sol.compareVersion("1.0", "1.0.0.0"))  # Output: 0
