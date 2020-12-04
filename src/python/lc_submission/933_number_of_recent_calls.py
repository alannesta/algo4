"""
https://leetcode.com/problems/number-of-recent-calls/

Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3

"""


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


class RecentCounter(object):

    def __init__(self):
        self.request_log = []
        self.window_start_idx = 0

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.request_log.append(t)

        while True:
            if self.request_log[self.window_start_idx] < t - 3000:
                self.window_start_idx += 1
            else:
                break

        self.request_log = self.request_log[self.window_start_idx:]
        self.window_start_idx = 0
        print(len(self.request_log))
        return len(self.request_log)



counter = RecentCounter()
counter.ping(642)
counter.ping(1849)
counter.ping(4931)
counter.ping(5936)
counter.ping(5957)


