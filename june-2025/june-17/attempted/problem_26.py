from typing import List

class Solution:

  def removeDuplicates(self, nums: List[int]) -> int:
    # case when there are no elements in nums
    if (len(nums) == 0):
      return 0
    # next index to put unique element
    k = 0
    for i in range(len(nums)):
      # if the number is unique, place in range
      if nums[i] != nums[k]:
        # open up next index
        k += 1
        nums[k] = nums[i]
    # add one to return the size not the last index
    return k + 1