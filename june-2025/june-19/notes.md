# Problems Completed
Easy: 0
Medium: 1
Hard: 0

## Problem 4: Group Anagrams

### Initialization

I initialized a default dictionary `res` that allows for its values to be a list that can be appended to.
The reason I used a `defaultdict` instead of a normal dictionary is that `defaultdict` allows for items to append
to a list assigned to a key that doesn't exist yet, rather than throwing an error.

### Algorithm

First, I created a for loop to loop through each string `s` in `strs`. Then, I used a similar approach as isAnagram
by creating a fixed array `count` that will store the count of each character in string `s`. Then, I created an inner for
loop to iterate through each character `c` in `s`, and updated the `count` array based on which characters were processed.

After exiting the inner loop, I added the string `s` to `res` based on its `count` signature. I made `count` into a tuple
before assigning it as a key because keys are meant to be immutable, and a feature of tuples is that they are immutable. Then,
I just appended `s` to the list mapped to the key from `tuple(count)`.

Finally, I return `list(res.values())`. `res.values()` will get all of the lists from `res`, which already has the strings
from `strs` grouped based on `count`. Then, I add those values into an outer list, so that each element of the outer list
is the group of strings that are anagrams of each other.

### Challenges

This was a very challenging problem, but I knew that there would be some similarities to isAnagram in terms
of keeping track of the count of the characters for each string. My failed attempt had a similar structure
to the real solution, but lacked some of the intuition for how to create the list of lists.

### Extra Notes

Had to find solution after failed attempt to form my own solution. I ended up learning about
`defaultdict`, which is a type of dictionary that does not throw an error when appending to a key
that does not exist yet.

There is another method that involves sorting the characters in the strings and then using a similar process.
I can also implement this without using a `defaultdict` by first checking if the key exists.

## Problem 5: Top K Frequent Elements

### Initialization

I initialized a dictionary `counts`, where the key is the unique number found in `nums`, and the value is
the frequency of that number.

I also initialized a list `res` to store the resulting `k` most frequent elements.

### Algorithm

First, I iterated through `nums` to process the counts of each number found. This time, I used a regular
dictionary instead of a default dictionary.

Next, I sorted the dictionary `counts` based on the value (the count), and then iterated through the sorted
dictionary until the `k` elements were added to `res`, or all unique numbers were added to `res` if there are less
numbers than `k`.

### Challenges

I wasn't sure how to sort the keys using the values, so I had to search it up.

### Extra Notes