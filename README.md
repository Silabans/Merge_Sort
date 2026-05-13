# Merge Sorting
A simple implementation of merge sorting (divide, sort and merge) in python without string slicing.

## Foundation
### Concepts
* Pointers for dividing a list into sublists
* Using temporary lists to compare the values within two different sublists
* Recursive thinking

### Time Complexity
The time complexity is O(nlog(n)), which is because of the following:
* Division into sublists => O(log(n)) => finding the mid-index as the dividing line of a list, similar to binary search
* Merging sublists into a sorted list => O(n) => iterating through the temporary lists to sort and merge
