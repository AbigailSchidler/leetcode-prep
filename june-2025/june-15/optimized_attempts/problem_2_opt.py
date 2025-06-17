# Num of times attempted: 3
# Is Optimal: True

class Solution:

  def romanToInt(self, s: str) -> int:
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    nums = []
    for i in range(len(s)):
      curr = values[s[i]]
      if i > 0:
        prev = nums[i - 1]
        if prev < curr and prev != 0:
          nums[i - 1] = curr - prev
          nums.append(0)
        else:
          nums.append(curr)
      else:
        nums.append(curr)
    return sum(nums)