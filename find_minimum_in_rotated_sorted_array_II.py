"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0; r = len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[r] < nums[mid]:
                # min is b/w mid and r
                l = mid + 1
            elif nums[r] > nums[mid]:
                # min lies to the left as in an unrotated array
                r = mid
            else:
                # we dont know  where the min lies, so we shorten the  search window 
                r -= 1
        return nums[l]