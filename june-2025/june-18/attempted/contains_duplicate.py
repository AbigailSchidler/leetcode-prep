# Interviewer Ready (shows algorithmic approach)

from typing import List

class Solution:

  def hasDuplicate(self, nums: List[int]) -> bool:
    found = set()
    for num in nums:
      if num in found:
        return True
      else:
        found.add(num)
    return False