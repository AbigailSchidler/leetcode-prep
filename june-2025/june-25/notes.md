# Problems Completed
Easy: 0
Medium: 2
Hard: 0

# Problems Revisited

Problem 5: Top K Frequent Elements

## Problem 5: Top K Frequent Elements - Revisited

### Notes

I realized I should attempt using bucket sort for this problem, so this was a good introduction to that
sorting technique.

I found it interesting that the list that was storing the buckets had a length of `len(nums) + 1`. After
thinking about it for a while, I realized that this is because there can be a case where the list `nums`
only has one unique number in it, so the frequency of that number would equal `len(nums)`. Since we are
labeling the buckets with the frequency using indices, I needed to add 1 to create that index of value `len(nums)`.

I also realized that the bucket at index 0 will always be empty. This makes it unnecessary to iterate through
when appending values to `res`. However, this list is still important because it helps line up the indices with
the counts when adding numbers to the buckets.

## Problem 6: Encode and Decode Strings (Medium)

### Approach

I knew for the encoding process, I could just iterate through each string in `strs` and append it to the
overall `res` string. The hints recommended formatting the encoded string to start with the length of the string,
then a character separating the length and the start of the string, and finally the string itself. So it was really
simple following that advice to create the optimal `encode` method.

For `decode`, I first thought about using conditionals to figure out how to decode the string. While that did end
up working in the end, it was very messy code. When I looked at the solution, I realized that I can make use
of string slices and start and end indices `i` and `j` to parse different parts of the encoded string.

### Challenges

`decode` was really difficult to figure out how to write optimally. I learned that I can utilize slices and indices
to navigate the decoding process more efficiently.

## Problem 7: Product of Array Except Self (Medium)

### Approach

It was really easy coming up with a solution, but it was more difficult coming up with an efficient one that does
not have O(n^2) time complexity. Looking at some optimal solutions, I learned that I can iterate through the array
twice, forwards and backwards, and use values called `prefix` and `postfix` to multiply to after an element has been
processed.

### Challenges

The main challenge was coming up with a more optimal solution than using a double for loop.