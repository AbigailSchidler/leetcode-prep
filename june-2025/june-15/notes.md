# Problems Completed
Easy: 1
Medium: 0
Hard: 0

## Problem 1: Palindrome Number (Easy)

### Approach

I wanted to approach solving this problem without the help of casting to a string. To do that,
I used mod and division to reverse the integer and compare, since if an integer is a palindrome,
its reversed state should equal the original. Negative numbers are not palindromes since only the
beginning of the value contains a negative sign.

### Initialization

I check if the number is negative first. This is the easiest case to check before going through the
process of reversing the integer.

Then, I saved the original integer `x` into another variable `orig` that will be modified when going
through the process of reversing the integer and saving it in another value `rev`, initialized to 0.

### Algorithm

The reversal process involves using % 10 on `orig` to retrieve the last digit. Next, I multiply the
current value of `rev` by 10 to move all of its digits up one, saving a space in the ones digit to
add `digit`. Finally, I remove the `digit` from `orig` by dividing `orig` by 10, thus moving the 10s
digit to the ones digit, if applicable.

After there are no more digits to loop through in `orig`, I check if the two integers `x` and `rev`
are equal. It returns `true` if they are palindromes and `false` otherwise.

### Challenges

It was challenging trying to figure out how to approach comparing the integer in a way to determine
if the front and back of the integer are the same. I knew I had to use mod and division in some way
in order to achieve this, but it was easier once I realized I could use another variable to store
a reversed string.