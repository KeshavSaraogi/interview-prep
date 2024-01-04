'''
A phrase is a palindrome if, 
after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s) == 0: return False
        if len(s) == 1: return True

        left = 0
        right = len(s) - 1

        while left < right:
            if (s[left].isalnum()):
                if (s[right].isalnum()):
                    if (s[left].lower == s[right].lower()):
                        left = left + 1
                        right = right - 1
                    else:
                        return False
                else:
                    right = right - 1
                    continue
            else:
                left = left + 1
                continue
        return True

