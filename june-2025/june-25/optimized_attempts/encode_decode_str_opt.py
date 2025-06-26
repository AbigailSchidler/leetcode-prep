# Interviewer Ready Solution

from typing import List

class Solution:

  def encode(self, strs: List[str]) -> str:
    res = ""
    for s in strs:
      res += str(len(s)) + "#" + s
    return res

  def decode(self, s: str) -> List[str]:
    res = []
    # start of string slice
    i = 0
    while i < len(s):
      # end of string slice
      j = i
      # increases slice range until delimeter is spotted
      while s[j] != '#':
        j += 1
      # casts slice into int to represent the size of string that follows
      length = int(s[i:j])
      # sets to beginning of string to decode
      i = j + 1
      # sets of end of string to decode
      j = i + length
      # adds the string to res
      res.append(s[i:j])
      # sets i to start after the decoded string
      i = j
    return res