# Interviewer Ready
# Number of times attempted: 2
# Is Optimal: True

from typing import List

class Solution:

  def twoSum(self, nums: List[int], target: int) -> List[int]:
    # dictionary where key = element in nums and value = index
    map = {}
    for i in range(len(nums)):
      # finds the value needed to add to target using nums[i]
      need = target - nums[i]
      # case when needed integer is found in the map from previous insertion
      if need in map:
        return [map[need], i]
      # case when needed integer is not found, so current value is added to map
      else:
        map[nums[i]] = i
    # case when there exists no integers that meet target value
    return [-1, -1]