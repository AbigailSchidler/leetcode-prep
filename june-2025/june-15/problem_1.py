class Solution:

  def isPalindrome(self, x: int) -> bool:
    # case when number is negative
    if x < 0:
      return False
    # saves original integer to modify
    orig = x
    # the reversed integer
    rev = 0
    # loops through all digits and puts them in reverse order
    while orig > 0:
      digit = orig % 10
      rev = rev * 10 + digit
      orig //= 10
    return x == rev