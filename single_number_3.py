"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xy = 0
        for n in nums:
            xy^=n
            
        xy&=-xy
        result = [0,0]
        for n in nums:
            if xy & n == 0:
                result[0]^=n
            else:
                result[1]^=n
        return result