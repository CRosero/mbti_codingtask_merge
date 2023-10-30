# MBTI Coding Task 2 
This git repository contains my solution for the MBTI Coding Task 2: 

Implement a function MERGE that takes a list of intervals and returns a list of intervals as result. In the result all overlapping intervals shall be remembered. All non-overlapping intervals remain untouched.

Example:

Input: [25,30] [2,19] [14, 23] [4,8] Output: [2,23] [25,30]

## Execution

The merge.py file contains the function merge, which can be executed directly in python or via the command line by calling 
```Shell
merge.py interval_list --test_function=False
```
whereas `interval_list` is a string containing the intervals to be merged. For example, it would be executed as 

```Shell
merge.py '[[1,3], [2,7]]'
```
with the output being:

```Shell
The input intervals have been merged to [[1, 7]].
```
`test_function` sets whether `merge.py`, if (by default) `False`, should execute the function merge with the desired input interval or, if `True`, execute it with several different inputs defined in the function `test_merge()` to test its fuctionality, by calling

```Shell
merge.py '[]' --test_function=True
```
with the output being:
```Shell
All tests passed.
```
if all tests passed, otherwise an AssertionError will be raised.
