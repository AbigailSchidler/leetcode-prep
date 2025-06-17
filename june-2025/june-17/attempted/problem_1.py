from typing import List


class Solution:

  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead
    """
    # the current element for list m
    # keeps track of how many elements have been processed for the first list
    mIdx = 0
    # the current element for list n
    # keeps track of how many elements have been processed for the second list
    # and its actual position in the list nums2
    nIdx = 0
    # the index pointing at the actual part of nums1
    resIdx = 0
    # while there are unprocessed elements in m and n
    while mIdx < m and nIdx < n:
      # case when element from list 1 is ge nums 2
      if nums1[resIdx] >= nums2[nIdx]:
        nums1.insert(resIdx, nums2[nIdx])
        # move to next n element
        nIdx += 1
      # case when element from list 1 is l nums 2
      else:
        # move to next m
        mIdx += 1
      resIdx += 1
    # while there are still unprocessed n elements (add to end)
    while nIdx < n:
      nums1[resIdx] = nums2[nIdx]
      resIdx += 1
      nIdx += 1
    # pops any remaining 0 padding at the end
    while len(nums1) > m + n:
      nums1.pop()