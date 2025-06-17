from typing import List

class Solution:

  def plusOne(self, digits: List[int]) -> List[int]:
    # adds one to the last element in digits, which represents the last digit
    digits[len(digits) - 1] += 1
    # while there exists more than one digit in a single digits element,
    # move the extra digit to the left
    while 10 in digits:
      # locates where the current 10 is
      index = digits.index(10)
      # changes the value of the current index to 0
      digits[index] = 0
      # case when 10 is at the front of digits
      if index == 0:
        # inserts the 1 in 10 at the front of the list
        digits.insert(0, 1)
      else:
        # increments the digit to the left of index by 1
        digits[index - 1] += 1
    return digits