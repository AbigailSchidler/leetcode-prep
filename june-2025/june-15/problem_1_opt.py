class Solution:

  def isPalindrome(self, x: int) -> bool:
    s = str(x)
    # s[::-1] reverses the string, makes it easy to compare
    return s == s[::-1]