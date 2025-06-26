from typing import List

class Solution:

  # matched the optimal solution
  def encode(self, strs: List[str]) -> str:
    res = ""
    for s in strs:
      res += str(len(s)) + "#" + s
    return res

  # really bad coding style!
  def decode(self, s: str) -> List[str]:
    res = []
    s_len = ""
    sub = ""
    size = 0
    for c in s:
      if size > 0:
        sub += c
        size -= 1
        if size == 0:
          s_len = ""
          res.append(sub)
          sub = ""
      elif c == '#':
        size = int(s_len)
        if size == 0:
          res.append("")
          s_len = ""
      else:
        s_len += c
    return res