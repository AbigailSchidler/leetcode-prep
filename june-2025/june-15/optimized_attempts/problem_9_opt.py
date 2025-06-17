# Interviewer Ready IF String conversion is allowed
# ELSE view problem_1.py
# Number of times attempted: 1
# Is Optimal: True

class Solution:

  def isPalindrome(self, x: int) -> bool:
    # convert integer to string
    s = str(x)
    # s[::-1] reverses the string, makes it easy to compare
    return s == s[::-1]