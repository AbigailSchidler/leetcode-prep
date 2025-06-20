from typing import List

class Solution:

  def twoSum(self, nums: List[int], target: int) -> List[int]:
    # looks at every element except last
    for i in range(len(nums) - 1):
      # starts one after index i until end of list
      for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
          return [i, j]