class Solution:
    def flipAndInvertImage(self, image):
        n = len(image)
        for row in image:
            for j in range((n + 1) // 2):  # Swap and invert in one pass
                row[j], row[n - j - 1] = row[n - j - 1] ^ 1, row[j] ^ 1
        return image
