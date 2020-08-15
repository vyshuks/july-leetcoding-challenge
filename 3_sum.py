"""
Given an array nums of n integers, are there elements a, b, c 
in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []

        # if nums is just zeroes return just one zeroes pair
        elif sum([i**2 for i in nums]) == 0:
            return [[0,0,0]]

        nums.sort()

        result = []


        for i in range(len(nums)):

            #duplicate skip it
            if i > 0 and nums[i]== nums[i-1]:
                continue

            # left pointer starts next to current i item
            l = i+1
            r = len(nums)-1

            while l< r:
                summ = nums[l] + nums[r]

                # if we find 2 numbers that sums up to -item
                if summ == -nums[i]:
                    result.append([nums[i],nums[l],nums[r]])
                    l +=1

                    # duplicate skip it
                    while l<r and nums[l] == nums[l-1]:
                        l +=1


                # if the sum is smaller than 0 we move left pointer forward
                elif summ + nums[i] < 0:
                    l +=1
                # if the sum is bigger than 0 move the right pointer backward   
                else:
                    r -=1

        return result