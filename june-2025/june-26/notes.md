# Problems Completed
Easy: 0
Medium: 1
Hard: 0

## Problem 8: Valid Sudoku (Medium)

### Approach

At first, I thought I had to split up the searches into three separate for loops to check the rows, cols, and
squares. I struggled to come up with an approach to check the squares, but I learned that I can section off the
squares using integer division (dividing the row and column values by 3).

Then, I learned that I can just use a single double for-loop to check all of the values at once, storing them
in `defaultdict`s.