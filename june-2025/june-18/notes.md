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

## Problem 2: Valid Anagram

### Approach

I figured that I could create list versions of the two strings to compare. I knew I couldn't use sets because
sets do not allow for duplicates, which could occur in words. Once I did this, I iterated through
`list_s` and checked if `list_t` contained each character in `list_s`. If it contained the character, that
character was removed from `list_t`. Otherwise, I returned `False` because it violates the definition of an
anagram.

After fully checking each character, I checked if the length of `list_t` was 0. If it was, then that means that
every character from `list_t` matched with every character from `list_s`, making it an anagram and returning `True`.
Otherwise, there are characters remaining in `list_t` that were not in `list_s`, violating the definition of an
anagram and returning `False`.

### Initialization

I initialized two lists `list_s` and `list_t` from strings `s` and `t` respectively. Each element in these
lists contained a character from the original strings.

### Algorithm

I looped through `list_s` and checked if `list_t` contained that character. If it did, then I removed that character
from `list_t`. Otherwise, I returned `False`.

After exiting the loop, I returned a boolean expression `return len(list_t) == 0`. This checks if there are characters
in `list_t` that were not found in `list_s`. The result of the expression matches whether the strings were anagrams of each
other or not.

### Challenges

At first I thought I could just return `list_s == list_t`. However, I learned that lists only equal if each element matches
the same order. This made me modify my approach to actually loop through one of the lists and check each element.

### Extra Notes

I can use a `count` function to check how many times each character appears in both strings. I just have to create a set
to hold all of the characters that occur in one string and compare it to the other string.

I can also just check for the size difference first to prevent the loop from being entered if the sizes are different,
which violates the definition of an anagram.

I learned that `count` is actually a costly function! It is better to use a fixed array of size 26 to keep track of the count
of the characters. (See isAnagramBetter in optimized solutions)

## Problem 3: Two Sum

### Approach

I used a brute force approach of just using an inner and outer for loop to check if the values at indices `i` and `j`
matched `target`. I figured this was not an optimal approach, but it was conceptually very easy to come up with this
solution.

### Extra Notes

I learned that mapping is a great way to make the code more efficient. I can map each of the values to an index by
creating a map titled `indices` and storing each value with an index. Then, I can loop through each of these key/value
pairs and find an instance of another key/value pair that matches the difference between the first value and target. If one
exists, then I found my two indices, and I return their keys.

With python, I can do this by using `enumerate` to gather the index and the value. `enumerate` returns like `i, n`, where
`i` is the index, and `n` is the value at that index.

I did not even need to use `enumerate` after all! I can just use a dictionary and assign keys as the value from
`nums` and the value as the index!