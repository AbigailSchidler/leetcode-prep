# Interviewer Ready
# Number of times attempted: 2
# Is Optimal: True

class Solution:

  # issue with this is count adds to time complexity! (O(n^2) in the worst case)
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    s_chars = set(s)
    for c in s_chars:
      # count is costly!
      if s.count(c) != s.count(t):
        return False
    return True

  def isAnagramBetter(self, s: str, t: str) -> bool:
    # checks if strings are same length
    if len(s) != len(t):
      return False
    # uses O(1) space since it's a fixed array
    char_count = [0] * 26
    for i in range(len(s)):
      # add one for every instance of char in s
      char_count[ord(s[i]) - ord('a')] += 1
      # subtract one for every instance of char in t
      char_count[ord(t(i)) - ord('a')] -= 1
    for i in range(len(char_count)):
      # checks if all chars canceled out -> is anagram
      if char_count[i] != 0:
        return False
    return True