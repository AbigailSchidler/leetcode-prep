# Problems Completed
Easy: 1
Medium: 0
Hard: 0

## Problem 1: Contains Duplicate

### Approach

This was a very simple problem where I can use a set to keep track of all elements found so far
in `nums`. I loop through `nums` once and check each element to see if it's currently in `found`.
If it is, then that means there is a duplicate in `nums` and `True` is returned. If the for loop exits
without returning `True`, then that means that `nums` does not contain any duplicates, and `False` is
returned.

### Initialization

I initialized a set named `found` that holds all unique elements found in `nums`. It is used as a comparing
tool against elements iterated through in `nums` to see if it has already been found in `nums` before, meaning
there is a duplicate.

### Algorithm

I use a for loop to iterate through each item in `nums`. If the current item is in `found`, then I return `True`
because that indicates there is a duplicate in `nums`. Otherwise, I add that element to `found`.

After the for loop terminates, I return `False` because all elements were processed in the for loop and didn't
show indication of a duplicate.

### Challenges

No challenges, but I wonder if I can just compare the size of `found` and `nums` at the end to see if they match.
If they do, then `False` is returned, and if they don't match, then `True` is returned, since sets contain no
duplicates as a feature of a set.

### Extra Notes

It is actually really easy to make a set out of the elements in `nums`. I can just use `set(nums)`, and then
compare the size of that and `nums` like I had thought. My original approach was a hash set approach, however.
This optimized approach would be considered hash set length. The hash set length approach is more consise
but not as algorithmic.