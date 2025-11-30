import heapq
def min_meeting_rooms(intervals):
    intervals.sort(key=lambda x:x[0])
    h=[]
    for s,e in intervals:
        if h and h[0] <= s: heapq.heappop(h)
        heapq.heappush(h,e)
    return len(h)
