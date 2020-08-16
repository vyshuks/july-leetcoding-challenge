"""
Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
        