'''
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.
Notice that you may not slant the container.
'''
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        water = 0

        while left < right:
            water = max(water, self.calculateWater(height, left, right))

            if (height[left] > height[right]):
                right = right - 1
            else:
                left = left + 1
        return water

    def calculateWater(self, height, a, b):
        return min(height[a], height[b]) * abs(a - b)