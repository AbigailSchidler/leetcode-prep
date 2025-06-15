# Problems Completed
Easy: 2
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

### Extra Notes

If I were to convert it to a string, I could compare it really easily through s == s[::-1], since that
slice automatically reverses the string. This is the fastest solution, but involves casting to a str.

## Problem 2: Roman to Integer (Easy)

### Approach

I decided to approach this by first storing the values of the roman numerals in a dictionary that can
be referenced throughout. While looping through the string and processing each of the roman numerals,
it is not enough to just look at one of the numerals at a time. I had to always check to see if the numeral
next to the first one was greater than, equal, or less than the first one. If the first numeral was >=, then
I only had to add the value it mapped to the resulting integer `res` that will be returned at the end. Otherwise,
I had to use both of the values for the first and second numerals and subtract second - first to get the value
to add to `res`. At the end, I double check that the last roman numeral was processed, and if it wasn't,
I add it to `res` and return the result.

### Initialization

I initalized a dictionary `values` that maps each of the roman numerals to their integer values. I also
initialized `res` to store the resulting conversion, `first` to represent the first char of the comparison pair,
and `second` to represent the second char of the comparison pair.

### Algorithm

I created a while loop that iterates while a pair of roman numerals to compare exists, which is checked
with `first` < `len(s)`.

In this while loop, I check if the first roman numeral is greater than or equal to the second. If true, it adds the first
roman numeral to `res` and increments the values of the indices by 1. Otherwise, it adds the subtraction of the numerals at `second` - `first` and adds the result to `res`.

Exiting the while loop, we check one last time if there is any unprocessed roman numeral remaining. If true, it adds that
mapped roman numeral value to `res`. Finally, `res` is returned.

### Challenges

A challenged I faced was an off-by-one error that was due to having one unprocessed roman numeral at the end.
It was an easy fix by checking the value of `first` to see if it maps to a valid last character in `s`.

### Extra Notes

It is more efficient to not have `first` and `second` index savers. I can instead use a `nums` array to store specific values
and sum the entire array at the end using `return sum(nums)`.