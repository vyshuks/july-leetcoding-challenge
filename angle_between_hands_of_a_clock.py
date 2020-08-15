"""
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

 

Example 1:

Input: hour = 12, minutes = 30
Output: 165
"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = (hour%12 + minutes/60)*30
        m = minutes*6
        angle = abs(h-m)
        return angle if angle <= 180 else 360-angle