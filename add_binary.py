"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
"""


from itertools import zip_longest

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result=[]
        for num1,num2 in zip_longest(a[::-1],b[::-1], fillvalue="0"):
            s = carry+int(num1)+int(num2)
            if s==0:
                result.append('0')
                carry=0
            elif s==1:
                result.append('1')
                carry=0
            elif s==2:
                result.append('0')
                carry=1
            elif s==3:
                result.append('1')
                carry=1
        if carry==1:
            result.append('1')
        return "".join(result[::-1])