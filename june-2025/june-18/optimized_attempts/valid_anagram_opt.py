# Interviewer Ready
# Number of times attempted: 1
# Is Optimal: True

class Solution:

  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    s_chars = set(s)
    for c in s_chars:
      if s.count(c) != s.count(t):
        return False
    return True