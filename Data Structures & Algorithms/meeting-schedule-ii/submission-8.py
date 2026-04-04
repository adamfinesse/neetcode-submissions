"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
        s,e,c = 0,0,0
        days = 0
        while s < len(start):
            if start[s] < end[e]:
                c+=1
                days = max(days,c)
                s+=1
            else:
                e+=1
                days = max(days,c)
                c-=1
        return days
