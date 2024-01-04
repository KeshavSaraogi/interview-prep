'''
Given an integer array nums, 
return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = set()

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                sums = nums[i] + nums[j] + nums[k]

                if (sums == 0):
                    result.add((nums[i], nums[j], nums[k]))                
                elif (sums > 0):
                    k = k - 1
                else:
                    j = j + 1
        return list[result]