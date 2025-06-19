class Solution:

  def isAnagram(self, s: str, t: str) -> bool:
    list_s = list(s)
    list_t = list(t)
    for c in list_s:
      # takes O(n) time worst case to see if element is in list!
      if c in list_t:
        # takes O(n) time worst case to remove element from list!
        list_t.remove(c)
      else:
        return False
    # checks the length difference too late!
    return len(list_t) == 0