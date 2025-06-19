# Interviewer Ready

from collections import defaultdict
from typing import List

class Solution:

  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # dictionary where key = tuple of character counts,
    # value = list of strings that match character counts
    res = defaultdict(list)
    for s in strs:
      # creates the fixed array to store count of each char
      count = [0] * 26
      for c in s:
        # increments count of char per occurrence in s
        count[ord(c) - ord('a')] += 1
      # adds string to list at assigned tuple key
      res[tuple(count)].append(s)
    # retrieves all lists from res and combines them into one list to return
    return list(res.values())