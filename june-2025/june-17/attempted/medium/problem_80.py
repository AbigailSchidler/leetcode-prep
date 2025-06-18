from typing import List

class Solution:

  def removeDuplicates(self, nums: List[int]) -> int:
    # next element index and number number of elements in correct list
    k = 1
    # number of duplicates for an element
    occur = 1
    for i in range(1, len(nums)):
      # case when element is a duplicate and it's only occurred once so far
      if nums[i] == nums[k - 1] and occur:
        nums[k] = nums[i]
        k += 1
        occur = 0
      # case when element is unique
      elif nums[i] > nums[k - 1]:
        nums[k] = nums[i]
        k += 1
        occur = 1
    return k