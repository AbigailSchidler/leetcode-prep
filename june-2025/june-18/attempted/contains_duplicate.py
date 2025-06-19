# Interviewer Ready (shows algorithmic approach)

from typing import List

class Solution:

  def hasDuplicate(self, nums: List[int]) -> bool:
    # set of characters found in nums array
    found = set()
    for num in nums:
      # case when found already contains the character
      if num in found:
        return True
      else:
        found.add(num)
    return False