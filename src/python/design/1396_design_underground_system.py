"""
https://leetcode.com/problems/design-underground-system/
"""
from collections import deque


class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.check_out = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        check_in_station = self.check_in[id][0]
        check_in_time = self.check_in[id][1]

        del self.check_in[id]

        key = (check_in_station, stationName)
        if key in self.check_out:
            self.check_out[key][0] += t - check_in_time
            self.check_out[key][1] += 1
        else:
            # [total time, count)
            self.check_out[key] = [t - check_in_time, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.check_out[(startStation, endStation)][0] / self.check_out[(startStation, endStation)][1]


# Your UndergroundSystem object will be instantiated and called as such:
"""
["UndergroundSystem","checkIn","checkIn","checkOut","checkIn","checkOut","checkOut","checkIn","getAverageTime","getAverageTime","checkIn","checkIn","getAverageTime"]

[[],[596854,"EQH524YN",13],[29725,"Y1A2ROGU",17],
[596854,"8AYN1B7O",115],[579716,"EQH524YN",145],[579716,"8AYN1B7O",199],
[29725,"8AYN1B7O",295],[939079,"16MTS56Z",371],["EQH524YN","8AYN1B7O"],
["Y1A2ROGU","8AYN1B7O"],[697035,"EQH524YN",442],[90668,"Y1A2ROGU",508],
["EQH524YN","8AYN1B7O"]]
"""
ops = ["UndergroundSystem", "checkIn", "checkIn", "checkOut", "checkIn", "checkOut", "checkOut", "checkIn",
       "getAverageTime", "getAverageTime", "checkIn", "checkIn", "getAverageTime"]
vals = [[], [596854, "EQH524YN", 13], [29725, "Y1A2ROGU", 17],
        [596854, "8AYN1B7O", 115], [579716, "EQH524YN", 145], [579716, "8AYN1B7O", 199],
        [29725, "8AYN1B7O", 295], [939079, "16MTS56Z", 371], ["EQH524YN", "8AYN1B7O"],
        ["Y1A2ROGU", "8AYN1B7O"], [697035, "EQH524YN", 442], [90668, "Y1A2ROGU", 508],
        ["EQH524YN", "8AYN1B7O"]]
obj = UndergroundSystem()

for op in zip(ops, vals):
    if op[0] == 'checkIn':
        obj.checkIn(*op[1])
    if op[0] == 'checkOut':
        obj.checkOut(*op[1])
    if op[0] == 'getAverageTime':
        print(obj.getAverageTime(*op[1]))
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
