# Interviewer Ready
# Number of times attempted: 2
# Is Optimal: True

from typing import List

class Solution:

  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    # current element being processed in nums1
    i = m - 1
    # current element being processed in nums2
    j = n - 1
    # refills the list backwards!
    k = m + n - 1
    # while there are still elements in nums2 not added to nums1
    while j >= 0:
      # case when there are still unprocessed elements in nums1
      # and the element in nums1 is greater than or equal to nums2
      if i >= 0 and nums1[i] >= nums2[j]:
        # overwrite kth index with nums1 element
        nums1[k] = nums1[i]
        # decrement to next element in nums1
        i -= 1
      # case when all elements in nums1 have been sorted
      # or element in nums2 is greater than element in nums1
      else:
        # overwrite kth index with nums2 element
        nums1[k] = nums2[j]
        # decrement to next element in nums2
        j -= 1
      # decrement to next space in overall nums1 to overwrite
      k -= 1
