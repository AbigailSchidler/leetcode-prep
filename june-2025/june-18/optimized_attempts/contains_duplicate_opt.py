# Interviewer Ready IF wanting a shortcut
# Number of times attempted: 1
# Is Optimal: True

from typing import List

class Solution:

  # hash set length approach
  def hasDuplicate(self, nums: List[int]) -> bool:
    return len(set(nums)) < len(nums)