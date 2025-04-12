def Merge_Overlapping_Subintervals(intervals):
    merged = []
    intervals.sort()

    for interval in intervals:
        # if no valid merge then append next interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        # else if there is valid merge, merge the interval and update the end value of the last interval of merged
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
        
    return merged


print(Merge_Overlapping_Subintervals([[1,3],[2,6],[8,10],[15,18]]))
print(Merge_Overlapping_Subintervals([[1,4],[4,5]]))