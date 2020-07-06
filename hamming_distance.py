"""
The Hamming distance between two integers is the
number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result, count = x^y, 0
        while result > 0:
            count += result & 1
            result >>= 1
        return count
