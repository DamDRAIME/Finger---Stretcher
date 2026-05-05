# https://leetcode.com/problems/insert-interval

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals
# still does not have any overlapping intervals (merge overlapping intervals if necessary).


def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    ni_start, ni_stop = newInterval
    if not intervals:
        return [newInterval]
    if ni_stop < intervals[0][0]:
        return [newInterval] + intervals
    if ni_start > intervals[-1][1]:
        return intervals + [newInterval]
    for i, (start, stop) in enumerate(intervals):
        if ni_start <= stop:
            if start > ni_stop:
                return intervals[:i] + [newInterval] + intervals[i:]
            start = min(ni_start, start)
            j = i + 1
            while j < len(intervals):
                j_start, j_stop = intervals[j]
                if ni_stop >= j_start:
                    stop = max(j_stop, ni_stop)
                    j += 1
                    continue
                break
            return intervals[:i] + [[start, max(stop, ni_stop)]] + intervals[j:]
