class Solution:

  def isAnagram(self, s: str, t: str) -> bool:
    list_s = list(s)
    list_t = list(t)
    for c in list_s:
      if c in list_t:
        list_t.remove(c)
      else:
        return False
    return len(list_t) == 0