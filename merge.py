def merge(interval_list):
    merged_list = []
    interval_list = sorted(interval_list)
    for interval in interval_list:
        if not merged_list:
            merged_list.append(interval)
        else:
            if interval[0] <= merged_list[-1][1]:
                print(interval[0])
                print(merged_list[-1][1])
                merged_list[-1][1] = max(merged_list[-1][1], interval[1])
            else:
                merged_list.append(interval)
    print(merged_list)
    return merged_list

if __name__ == '__main__':
    intervals = [[2,6],[1,3],[8,10],[15,18]]
    
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    assert merge(intervals) == [[1,6],[8,10],[15,18]]

    intervals_2 = [25,30], [2,19], [14, 23], [4,8]
    assert merge(intervals_2) == [[2,23],[25,30]]

    intervals_neg_num = [-1,10], [2,117], [14, 23], [4,8]
    assert merge(intervals_2) == [[2,23],[25,30]]

    intervals_inf_1 = [[float('-inf'),4],[0,4]]
    assert merge(intervals_2) == [[2,23],[25,30]]
    
    intervals_inf_2 = [[float('-inf'),4],[0,4]]
    assert merge(intervals_2) == [[2,23],[25,30]]
    
    intervals_inf_3 = [[float('-inf'),4],[0,4]]
    assert merge(intervals_2) == [[2,23],[25,30]]

    intervals_float= [[float('-inf'),4],[0,4]]
    assert merge(intervals_2) == [[2,23],[25,30]]

    intervals_double = [[float('-inf'),4],[0,4]]
    assert merge(intervals_2) == [[2,23],[25,30]]