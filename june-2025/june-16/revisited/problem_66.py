# Interviewer Ready Solution
# Num of times attempted: 1
# Optimal: True

from typing import List

class Solution:

  def plusOne(self, digits: List[int]) -> List[int]:
    # loop through the list backwards
    for i in range(len(digits) - 1, -1, -1):
      # if adding to the current digit will not cause overflow to 10, it's returnable
      # after addition
      if digits[i] < 9:
        digits[i] += 1
        return digits
      # otherwise digit is changed to zero and addition will attempt on next digit
      digits[i] = 0
    # case when front digit of list was 9, meaning a new digit must be added to front
    return [1] + digits