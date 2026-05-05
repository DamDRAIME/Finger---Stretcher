# https://leetcode.com/problems/merge-intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an
# array of the non-overlapping intervals that cover all the intervals in the input.


def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda interval: interval[0])
    merged_intervals = []
    prev_interval = intervals[0]
    for interval in intervals[1:]:
        if interval[0] <= prev_interval[1]:
            prev_interval = [prev_interval[0], max(prev_interval[1], interval[1])]
            continue
        merged_intervals.append(prev_interval)
        prev_interval = interval
    merged_intervals.append(prev_interval)
    return merged_intervals
