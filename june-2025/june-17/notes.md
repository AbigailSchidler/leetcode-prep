# Problems Completed
Easy: 1
Medium: 0
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

Another solution I found first had an if statement of `if `