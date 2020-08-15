"""
Reverse bits of a given 32 bits unsigned integer.
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        rep = list("{:032b}".format(n))
        rep.reverse()
        return int("".join(rep), 2)
