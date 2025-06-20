# Interviewer Ready Solution
# Num of times attempted: 1
# Optimal: True

class Solution:

  def romanToInt(self, s: str) -> int:
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    for i in range(len(s)):
      if i+1 < len(s) and values[s[i+1]] > values[s[i]]:
        res -= values[s[i]]
      else:
        res += values[s[i]]
    return res