class Solution:

  def romanToInt(self, s: str) -> int:
    # maps all of the roman numerals to their integer values
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # the resulting integer
    res = 0
    # first char index
    first = 0
    # second char index
    second = 1
    # while there are at least 2 chars in the str to compare
    while first < len(s) - 1:
      # case when first char is greater than or equal to second (add only first char)
      # skips just that added char
      if values[s[first]] >= values[s[second]]:
        res += values[s[first]]
        first += 1
        second += 1
      # case when first char is less than second (subtract first from second then add)
      # skips the whole pair
      else:
        res += values[s[second]] - values[s[first]]
        first += 2
        second += 2
    # off by one case when there is still one char to process
    if first == len(s) - 1:
      res += values[s[first]]
    return res