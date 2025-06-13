# Problems Completed
Easy: 0
Medium: 0
Hard: 0

# Problem 1: Maximum Number of Occurrences in a Substring

## Approach

### Initialization

I first thought to try using a sliding window approach starting at the beginning of the string.
I can save the start and end indices of the substring in `left` and `right` variables that expand
and contract based on the conditions of the substring.

I also have a variable storing the `size` of the substring, which I realize can also be computed with
`right` - `left` + 1. This helps to ensure the size of the substring does not fall outside the range
[`minSize`, `maxSize`].

Finally, I created a set `letters` that will store all of the unique characters in the substring, which
is added and removed from based on the conditions of the substring. This helps to ensure the size of the
set, or the number of unique characters in the substring, does not exceed `maxLetters`.

### Algorithm

TODO

## Challenges