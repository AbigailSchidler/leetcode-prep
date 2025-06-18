from typing import List

class Solution:

  def removeElement(self, nums: List[int], val: int) -> int:
    k = len(nums)
    # loops backwards so indices remain accurate
    for i in range(len(nums) - 1, -1, -1):
      if nums[i] == val:
        nums.pop(i)
        k -= 1
    return k