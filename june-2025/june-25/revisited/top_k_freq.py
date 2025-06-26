# Interviewer Ready

from typing import List

class Solution:

  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # stores the count for each instance of a number in nums
    # key: num, value: count of num
    count = {}
    # stores the numbers in nums that have a certain count
    # bucket sorting!
    freq = [[] for i in range(len(nums) + 1)]
    # calculates the count for every number in nums
    for num in nums:
      count[num] = 1 + count.get(num, 0)
    # adds each number to the correct frequency bucket
    for num, cnt in count.items():
      freq[cnt].append(num)
    res = []
    # iterates backwards through each bucket (highest freq first)
    for i in range(len(freq) -1, 0, -1):
      # keeps appending from buckets until k length is met
      for num in freq[i]:
        res.append(num)
        if len(res) == k:
          return res
    # case when there are less than k elements
    return res