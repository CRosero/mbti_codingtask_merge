def merge(interval_list):
    merged_list = []
    interval_list = sorted(interval_list)
    for interval in interval_list:
        if not merged_list:
            merged_list.append(interval)
        else:
            if interval[0] <= merged_list[-1][1]:
                # print(interval[0])
                # print(merged_list[-1][1])
                merged_list[-1][1] = max(merged_list[-1][1], interval[1])
            else:
                merged_list.append(interval)
    print(merged_list)
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
    test_merge()