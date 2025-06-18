# Interviewer Ready
# Number of times attempted: 2
# Is Optimal: False

from typing import List

class Solution:

  # two pointer example
  def removeElement(self, nums: List[int], val: int) -> int:
    # next index to fill with element not equal to val
    # and count of number of elements not equal to val
    # cool double usage!
    k = 0
    for i in range(len(nums)):
      # case when number at position does not equal val
      if nums[i] != val:
        # assign current index k to value not equal to i
        nums[k] = nums[i]
        # update count and next position to add a number not equal to value
        k += 1
    # return the number of elements not equal to number
    return k