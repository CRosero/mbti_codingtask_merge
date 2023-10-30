import argparse
import json

# Python program to merge overlapping Intervals in
# O(n Log n) time and O(n) extra space
def merge(interval_list):
    merged_list = []
    interval_list = sorted(interval_list)
    # Go through each interval in the list
    for interval in interval_list:
        # If the merged list is empty, add the first interval
        if not merged_list:
            merged_list.append(interval)
        else:
            # If the current interval overlaps with the last interval in 
            # the merged list, merge the two intervals
            if interval[0] <= merged_list[-1][1]:
                merged_list[-1][1] = max(merged_list[-1][1], interval[1])
            # If the current interval does not overlap with the last interval in 
            # the merged list, add the current interval to the merged list
            else:
                merged_list.append(interval)
    return merged_list

def test_merge():
    
    # Test case ascending
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    assert merge(intervals) == [[1,6],[8,10],[15,18]]

    # Test case descending
    intervals_inv = [[15,18],[8,10],[2,6],[1,3]]
    assert merge(intervals_inv) == [[1,6],[8,10],[15,18]]

    # Test case overlapping (from the example given in the task description)
    intervals_ex = [[25,30], [2,19], [14, 23], [4,8]]
    assert merge(intervals_ex) == [[2,23],[25,30]]

    # Test case negative numbers
    intervals_neg_num = [[-11,3],[2,6],[8,10],[15,18]]
    assert merge(intervals_neg_num) == [[-11,6],[8,10],[15,18]]

    # Test case negative infinity
    intervals_inf_1 = [[float('-inf'),4],[0,8]]
    assert merge(intervals_inf_1) == [[float('-inf'),8]]
    
    # Test case negative and positive infinity
    intervals_inf_2 = [[float('-inf'),4],[0,float('inf')]]
    assert merge(intervals_inf_2) == [[float('-inf'),float('inf')]]
    
    # Test case positive infinity
    intervals_inf_3 = [[0,4],[3,float('inf')]]
    assert merge(intervals_inf_3) == [[0,float('inf')]]

    # Test case float numbers
    intervals_float= [[-1.5,4],[0,5]]
    assert merge(intervals_float) == [[-1.5,5]]

if __name__ == '__main__':
    # Parse arguments from command line
    parser = argparse.ArgumentParser("Interval merge function.")
    parser.add_argument("interval_list", type=json.loads, help="List of intervals to merge.")
    parser.add_argument("--test_function", type=bool, default=False, help="Boolean used to test the function.")
    args = parser.parse_args()

    # Run test function if specified
    if args.test_function:
        test_merge()
    else:
        # Run merge function
        merged_interval_list = merge(args.interval_list)
        print(f"The intervals {args.interval_list} have been merged to {merged_interval_list}.")