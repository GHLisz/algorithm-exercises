class Solution:
    """
    @param time: the given time
    @return: the next closest time
    """
    def nextClosestTime(self, time):
        # write your code here
        s = set(time)
        hour, minute = int(time[:2]), int(time[3:])
        while True:
            minute += 1
            if minute == 60:
                minute = 0
                hour = 0 if hour == 23 else hour + 1
            time = "%02d:%02d" % (hour, minute)
            if set(time) <= s:
                return time
