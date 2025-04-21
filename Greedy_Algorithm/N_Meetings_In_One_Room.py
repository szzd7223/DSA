def maxMeetings(start, end):
    n = len(start)
    meetings = []
    ans = []

    for i in range(n):
        meetings.append((start[i], end[i], i)) # This basically makes a data structure with meeting info

    meetings.sort(key=lambda x: x[1]) # This sorts the meetings list in ascending order of end time

    count = 0
    last_end_time = -1

    for s, e, i in meetings:
        if s > last_end_time:
            count += 1
            last_end_time = e
            ans.append(i)
    
    return [count, ans]

start = [1,3,0,5,8,5]
end = [2,4,6,7,9,9]
print(maxMeetings(start, end))

