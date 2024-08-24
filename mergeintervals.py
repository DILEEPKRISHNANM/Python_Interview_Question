# def merge_intervals(intervals):
#     if not intervals:
#         return []
    
#     intervals.sort(key=lambda x: x[0])
#     merged = [intervals[0]]
    
#     for current in intervals[1:]:
#         last = merged[-1]
#         if current[0] <= last[1]:
#             last[1] = max(last[1], current[1])
#         else:
#             merged.append(current)
    
#     return merged

# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# print(merge_intervals(intervals))  # Output: [[1, 6], [8, 10], [15, 18]]



def mergeintervals(interval):
    if not interval:
        return []

    interval.sort(key = lambda x:x[0])
    merged = [interval[0]]
    for current in interval[1:]:
        last = merged[-1]
        if last[1]>= current[0]:
            last[1] = max(current[1],last[1])

        else:
            merged.append(current)


    return merged
interval = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(mergeintervals(interval))
