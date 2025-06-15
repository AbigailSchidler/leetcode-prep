# Num of times attempted: 1
# Is Optimal: False

class Solution:

  def romanToInt(self, s: str) -> int:
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    nums = []
    for i in range(len(s)):
      if i > 0:
        continue
      else:
        nums.add(values[s[i]])
    return sum(nums)