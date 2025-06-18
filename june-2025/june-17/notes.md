# Problems Completed
Easy: 3
Medium: 1
Hard: 0

## Problem 88: Merge Sorted Array (Easy)

### Approach

I decided to loop through each of the elements in both of the lists until all of the elements in the
first list or second list are processed. During this process, I check which of the two elements
from both lists is larger, and either place the element from `nums2` before the element in `nums1`,
or move on to the next element in `nums1`. This continues until either one of the lists are fully
processed.

After this, I double check that all of the elements `nums2` are processed. If not, then that means
that they should be added to the end of the list in `nums1`, since this case only happens when the remaining
elements in `nums2` are larger than all elements in `nums1`.

Once this is complete, I remove any extraneous padding of zeros at the end of `nums1` until the length of
`nums1` matches `m + n`.

### Initialization

I initialized 3 variables. `mIdx` keeps track of the number of elements that were processed from `nums1`.
`nIdx` keeps track of the number of elements processed from `nums2`, as well as the actual indexed position
within `nums2`. `resIdx` keeps track of the actual position of the element from `nums1`, since elements from
`nums2` are being inserted in `nums1`.

### Algorithm

The first while loop iterates through the elements in `nums1` and `nums2` and checks which element is larger.
Note that I used `resIdx` to check the element in `nums1` because with the insertion of elements in `nums2` into
`nums1`, `mIdx` does not correctly reflect the position of the next element.

If the element in `nums1` is greater than or equal to `nums2`, then I insert the value of `nums2` at `resIdx`,
which moves everything currently in `nums1` starting at `resIdx` to the right of that element. Then, I update
`nIdx` since the element was processed and placed in the correct part of the sorted list.

Otherwise, the element in `nums1` is less than `nums2`, so I update `mIdx` to show that the element in `nums1`
is in the correct position.

At the end of this loop iteration, I update `resIdx` by one to keep track of the current element from `nums1`
to compare next. This is either the same element compared earlier that was moved by one because the element from
`nums2` was inserted, or a new element from `nums1` that was moved to because the previous element from `nums1` was
processed.

After the first while loop terminates, I checked that all elements from `nums2` were processed, meaning they were
placed in `nums1`. If there are any elements left unprocessed, they are added to the end of `nums1`, located by the
position of `resIdx` since there is padding at the end of `nums1` that does not represent actual elements in `nums1`.

After all elements have been processed, I run iterations of popping the end of `nums1` until the length of `nums1`
equals `m + n`.

### Challenges

The main challenge I experienced was having to keep track of positions of elements to compare. At first, I thought
I only needed to keep track of `mIdx` and `nIdx`, but since I had to add the elements in `nums1` instead of a new list,
the value of `mIdx` did not always accurately reflect the position of the next element originally from `nums1`.

My solution was to add another variable `resIdx` that keeps track of the actual position of the original element in
`nums1`. That way `mIdx` only keeps track of how many elements have been processed from `nums1`.

### Extra Notes

Another solution I found first had an if statement of `if not nums1 and nums2` then `return None`. I'm not sure
if that is required, since my solution does not include this statement.

Otherwise, this other solution uses the process of iterating through the `nums2` backwards, which makes it simpler
having to only loop through the values in `nums2`. I noticed that they also had three variables declared, but instead
of starting at 0, they started at the end of the range for each of the variables.

## Problem 27: Remove Element (Easy)

### Approach

This problem was very simple. I chose to save the number of elements not equal to `val` in a variable `k` that is
set to the length of `nums`, and subtracting whenever I find an occurence of `val`, but I could have also set `k`
to 0 and incremented whenever I don't find an instance. I figured the first approach was better, however.

When `val` was found in the `nums`, I used `pop(i)` to remove the element at index `i` from `nums`. To ensure that this
worked after an element was removed, I iterated through `nums` backwards. This also ensured that all elements not equal
to `val` would be found at the front of `nums`.

### Initialization

I only initialized one variable `k` set to the length of `nums`. I chose this approach because assuming I kept the same if branch in my code `if nums[i] == val`, I would need an `else` branch to increment `k` if `k` was initialized to 0. Setting `k`
to `len(nums)` seemed like a cleaner approach with less branches.

### Algorithm

Because I was tasked to remove elements from `nums`, I chose to iterate through `nums` backwards so as to not disrupt the
indexing in the for-loop. Within the loop, if I found `val` at the index `i`, I used `pop(i)` to remove the element from the
list. If I were to iterate starting at index 0, this would have disrupted the loop and could have led to skipping values
that should be removed. I also decremented the value of `k` whenever `val` was found in `nums`. At the end, I returned `k`.

### Challenges

The biggest challenge was understanding what constitutes something as being `in-place`. I was unsure if using `pop(i)` was
a cheat code to removing the elements. Am I supposed to leave the size of `nums` unchanged, and still remove the elements
somehow? I have to check other solutions. If not, I believe this solution I came up with is optimal.

### Extra Notes

Looking over solutions, I realized that using `pop(i)` is very costly, which can give me a runtime of `O(n^2)`. I need to use
a two-pointer approach instead, where I leverage `k` to start at 0 and basically give the index position of the element that
is not equal to `val`. I'm not actually deleting from the list! Instead I overwrite the first `k` elements of `nums` to hold
all values that do not equal `val`.

## Problem 26: Remove Duplicates From Sorted Array (Easy)

### Approach

I realized that this problem was very similar to problem 27 in terms of using a two pointer approach to keep track of
the next element to process `i` in terms of whether it's a duplicate or not, and the next spot to place a unique element
with `k`. The only difference was that I couldn't rely on `k` to store the final count of unique elements in the end,
and I needed a base case that handled empty lists. Since `k` was only off by one, I added 1 to the return statement to get
the final result.

### Initialization

First, I checked if `nums` was empty. If so, I just returned 0. Otherwise, I initialized a variable `k` with a much
similar purpose as in problem 27.

### Algorithm

The overall loop and body of the for loop were structurally similar to problem 27 with some tweaks. If `nums[i] != num[k]`,
then I moved the index of `k` over one to accommodate for the next unique element spot. Then, I placed the value of
`nums[i]` in `nums[k]`.

After exiting the loop, I returned `k + 1` because `k` only stored the last index of the unique elements, not the actual size,
which is easily fixed by adding one.

### Challenges

I briefly struggled with thinking about how to use the knowledge from problem 27 to modify into a working solution for
problem 26. I am still unsure if there was a simpler way to modify my solution for problem 27.

### Extra Notes

Read the constraints! One of the constraints is that `nums` is guaranteed to have at least one element, so I did
not need the base case! This makes it way easier to match with problem 27 in that I can start at `k = 1` instead
of `k = 0`. That way I can continue to use it as a pointer for the next open spot for a unique value, and the actual
count of unique elements.

## Problem 80: Remove Duplicates from Sorted Array II (Medium)

### Approach

This problem was very similar to problem 26. At this point I had not attempted the optimized solution I found for problem
26, but I chose to try using that logic to implement this problem anyway. The only difference for this problem was that if
a duplicate was found, it is allowed to be added to the final array if it's only the second occurrence. Therefore, I kept
track of a new variable `occur` that remembered if an element was already added. The other case followed the same logic
as problem 26 in terms of if the element was unique.

### Initialization

I initialized two variables. The first was `k`, which was set to 1 because the constraints specify that `nums` has at least
one element.

The second variable was `occur`, which I initialized to 1 also because there was one occurrence of the first value in `nums`
that was processed. This value would either be 0 or 1 (may change to be True or False) based on whether a duplicate was found
or another unique value.

### Algorithm

The for loop went from the range [1, len(s)) because the first element of the array was already processed as valid.

The first condition in the body of the for loop checks for a case when the compared elements are the same, and there's only
been one occurrence of that element so far. The second condition is identical to problem 26 in seeing if `nums[i] > nums[k-1]`.
Both of these conditions check for a valid element to add, so the bodies of these conditionals are almost identical, with the exception of setting `occur` to 0 for the first condition, and 1 for the second. I believe there is a less redundant way to approach this.

`k` is returned at the end since it represents the number of elements that should remain in the list.

### Challenges

My main challenge was trying to reduce redundancy in my code, which I will have to check with a sample solution to get advice.

### Extra Notes

One of the sample solutions is SO similar to problem 26 with one tweak. Instead of using `k=1` and `nums[k-1]`, it goes in pairs of twos! This means it uses `k=2` and `nums[k-2]`. So simple!!! There is no need for the `occur` variable with this approach.