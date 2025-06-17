class Solution:

  def addBinary(self, a: str, b: str) -> str:
    # convert the strings to lists where each element contains a binary digit
    a_list = list(a)
    b_list = list(b)
    # case when len(a) > len(b)
    if len(a) > len(b):
      while len(a_list) > len(b_list):
        b_list.insert(0, '0')
    # case when len(a) < len(b)
    elif len(a) < len(b):
      while len(a_list) < len(b_list):
        a_list.insert(0, '0')
    # adds each binary digit from a and b into a total
    total = [int(x) + int(y) for x,y in zip(a_list, b_list)]
    # while there is an invalid binary digit, correct by moving over to left
    while 2 in total:
      index = total.index(2)
      # sets curr index to 0
      total[index] = 0
      # case when invalid digit is in front of list
      if index == 0:
        total.insert(0, 1)
      # case when invalid digit is not at front of list
      else:
        total[index - 1] += 1
    # converts the digits back to chars
    total_chars = [str(x) for x in total]
    return "".join(total_chars)