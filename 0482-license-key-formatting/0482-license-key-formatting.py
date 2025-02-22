class Solution(object):
    def licenseKeyFormatting(self, s, k):
        s = s.replace("-", "").upper()[::-1]  # Remove dashes, uppercase, reverse
        groups = ["".join(s[i:i+k]) for i in range(0, len(s), k)]  # Group every k
        return "-".join(groups)[::-1]  # Join and reverse back