# Problems Completed
Easy: 0
Medium: 0
Hard: 0

# Problems Revisited
Problem 1: Roman to Integer (Easy) - Attempted Last on June 15

Problem 66: Plus One (Easy) - Attempted Last on June 15

Problem 67: Add Binary (Easy) - Attempted Last on June 15

## Problem 1: Roman to Integer (Easy) - Revisited

### Notes

I was struggling to memorize the "optimal" solution I found yesterday, and I figured there is
probably a simpler solution that is the true solution looked for. I found it, where it only uses
one index variable to loop through the string and uses compound assignment operators -= and +=
based on the two conditions.

The first condition is when another character after the one at `i` is found and that character has
a higher value than the character at `i`, in which case we can subtract `i` from `res`.

The second condition is used when either another character after `i` does not exist or the character
at `i` has a higher value than `i+1`, in which case we add `i` to `res`.

This is a much simpler approach to my original solution and the solution I found after.

## Problem 66: Plus One (Easy) - Revisited

### Notes

While I was trying to find optimal solutions, I realized that some of the ones I was finding may
not be considered good for an interview setting, since interviewers mostly look for algorithmic
thinking, rather than quick one-liners. I checked with ChatGPT with one of these solutions and compared
it with my own, and it told me that while my solution was better for an interview setting, I was using
costly functions like `insert` and `index` in my code for addBinary. I realized that since my logic for
addBinary was similar to plusOne, that I had these same costly function usages in my solution here.

It was suggested that instead of using index to always find the troublesome index, I can instead iterate
through the list backwards, starting at the least significant digit and working up to the top. Then, I
checked the digit starting from the bottom to see if adding 1 to it would cause the element to overflow to
two digits in one element (10). If not, then I can add one to the current digit and return the result,
since the process of adding one was successful. Otherwise, I changed the value of the digit from 9 to 0,
and iterated to the next element, which could potentially add that carried over 1 to its element or carry
it again.

## Problem 67: Add Binary (Easy) - Revisited

I tried a similar approach to the new plus one solution, but also learned to use a carry variable, since
this is more difficult than just adding 1 to a number. By reversing the iteration direction for `a` and `b`,
it saved more space overall. It was easier to add the numbers together by adding the current binary digit
value to `carry`, and processing the result of `carry` after.

I saved each of the binary digits in a list that can be joined into a string later. These values were input in
reverse order because I looped from the end of the strings to the beginning. For each digit, I added the value
based on the value of `carry % 2`, since it holds any values added from `a` and `b`. Then, I used integer division
by 2 on `carry` to show that the value caused from the addition was either added to the current digit or
carried over to the next digit.

At the end, since `res` was reversed, I used a join on an empty string with the reversed `res`.