# Problems Completed
Easy: 4
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

## Problem 3: Plus One (Easy)

### Approach

My approach in adding one to the integer was very simple by adding one to the last element in `digits` through `digits[len(digits) - 1] += 1`. After this, I realized that there are cases when the last digit is 9, and adding 1 to it makes it 10, which does not follow the correct formatting of the list `digits`. I knew that I had to find a way to move over that digit by one, which brought up another issue where the original number was 99, or 999, or anything with a long list of 9s. I quickly figured out I can just locate where the current issue digit element is and update accordingly.

When the issue digit was at the front of the list, I had to add another element to `digits` at the front of the list to
accomodate for the new 1 to add to `digits`.

### Initialization

There was little initialization in this problem. The first step was just to add one to the last element in the list.

### Algorithm

If the last digit in `digits` was 9, we entere into a while loop that continues to find any 10s in `digits` and reformats it to the correct format of only one digit per element in `digits`.

While there still existed a 10 in the list, I located the problem element and set `digits[index]` to 0. Then, I split into
cases based on the placement of the problem element.

If the problem element was at the front (index 0), then I appended another element to the front of `digits`
and assigned its value to 1. Otherwise, I add 1 to the element located at `index - 1`.

Finally, I return `digits`.

### Challenges

The main challenge was trying to remember how to find the location of a digit element to fix, as well as append
to the front of the list. Both were easy to figure out by looking up documentation about a list in python.

### Extra Notes

This is an optimal solution!

## Problem 4: Add Binary (Easy)

### Approach

This problem was very similar to the previous one, where instead of base 10 digits, I was dealing with binary, and
I was adding two binary strings instead of adding one to a value.

To make the implementation somewhat similar to problem 3, I converted the strings into lists where each element is
a digit. Then, I made sure that both lists were the same length, so that each of the digits lined up properly for
adding. When I added them together into another list `total`, that is where I utilized methods from problem three to
fix any trouble digit elements so that it represents an authentic binary sequence. Finally, I converted the result back into
a binary string.

### Initialization

I initalized the method by converting strings `a` and `b` into lists, where each element represents a binary digit (0 or 1).

Next, I formatted the lists so that they are of equal length so that the addition matches up the digits properly. If
`a` was longer, then I added 0s to the start of `b_list` until the lengths matched. If `b` was longer, I added 0s to the start of `a_list` until the lengths matched.

Finally, I added the two lists together by converting each digit from `a_list` and `b_list` into integers and adding them
into `total`.

### Algorithm

The while loop in this problem follows the same logic as problem 3, where it continues to find any instances of 2 being in a
digits element, and fixing it so that it only shows a 0 or 1.

At the end, I convert the list back into a list of characters, and join the list together into a binary string to return.

### Challenges

The most challenge I had with this problem was converting strings to lists and back into strings later. I also had issues
with going from `total` back to a returnable string. I had to create `total_chars` as a crossing point so that the
`join` function on an empty string will work.

### Extra Notes

Most optimal solution utilizes a built in function of python `bin`, as well as `int` casting that also utilizes a parameter
`base`, which can be set to base 2 for binary. `bin()` always starts with `0b`, which needs to be sliced out of the string returned by `bin`.