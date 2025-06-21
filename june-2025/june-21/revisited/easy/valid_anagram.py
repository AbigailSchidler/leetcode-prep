# Interviewer Ready

class Solution:

  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    count = [0] * 26
    for i in range(len(s)):
      count[ord(s[i]) - ord('a')] += 1
      count[ord(t[i]) - ord('a')] -= 1
    for c in range(len(count)):
      if count[c] != 0:
        return False
    return True