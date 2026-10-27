class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1  # Add 1 if the last bit is set
            n >>= 1         # Shift right by 1
        return count