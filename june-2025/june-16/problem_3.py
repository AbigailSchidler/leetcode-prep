class Solution:

  def addBinary(self, a: str, b: str) -> str:
    res = []
    # the digit to carry to the next part of res
    carry = 0
    # the current indices of a and b, starting at the end of the string
    aIdx, bIdx = len(a) - 1, len(b) - 1
    # while there are still unprocessed a or b digits, or there is a digit to carry
    while aIdx >= 0 or bIdx >= 0 or carry == 1:
      # case when there is an unprocessed digit from a
      if aIdx >= 0:
        carry += int(a[aIdx])
        aIdx -= 1
      # case when there is an unprocessed digit from b
      if bIdx >= 0:
        carry += int(b[bIdx])
        bIdx -= 1
      # appends the remainder in base 2 of the addition
      res.append(str(carry % 2))
      # gives the carry over value for the next iteration
      # if the digits amounted to 0 or 1, then no carryover,
      # otherwise it amounts to 2 and is carried over
      carry = carry // 2
    return "".join(res[::-1])