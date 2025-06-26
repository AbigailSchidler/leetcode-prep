from collections import defaultdict
from typing import List

class Solution:

  def isValidSudoku(self, board: List[List[str]]) -> bool:
    # key: row # val: set containing nums in row
    rows = defaultdict(set)
    # key: col # val: set containing nums in cols
    cols = defaultdict(set)
    # key: square row/col pair val: set containing nums in square
    squares = defaultdict(set)

    for r in range(9):
      for c in range(9):
        val = board[r][c]
        # case when value is empty
        if val == '.':
          continue
        # case when a duplicate number is found in a row, column, or square
        if (val in rows[r] or val in cols[c] or val in squares[(r // 3, c // 3)]):
          return False
        # add the value to the correct row, col, and square
        rows[r].add(val)
        cols[c].add(val)
        squares[(r // 3, c // 3)]
    return True