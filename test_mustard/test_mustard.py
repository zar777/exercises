import math


class Solution:

    # parse the log file and insert it into a dictionary
    def parse_log(self,log):
        lines_log = log.split("\n")
        map_log = {}
        time_class = None
        for el in lines_log:
            line = el.split(",")
            if line[1] not in map_log:
                map_log[line[1]] = []
            time = line[0].split(":")
            time_class = Duration(time[0], time[1], time[2])
            map_log[line[1]].append(time_class)

        return map_log

    def free_number(self,map_log):
        max = 0
        string_max_number = ""
        time_seconds = 0
        for key in map_log:
            for index, el in enumerate(map_log[key]):
                    time_seconds += el.duration_seconds()
            if time_seconds > max:
                max = time_seconds
                string_max_number = key
            elif time_seconds == max:
                previous_number = int(string_max_number.replace("-", ""))
                key_number = int(key.replace("-", ""))
                if key_number < previous_number:
                    string_max_number = key_number
            time_seconds = 0
        return string_max_number

    def compute_price(self, duration):
        price = 0
        seconds = duration.duration_seconds()
        minutes = float(seconds) / 60
        if minutes < 5:
            price += seconds * 3
        else:
            price += int(math.ceil(minutes)) * 150
        return price

    def solution(self, log):
        payment = 0
        map_log = self.parse_log(log)
        free_number = self.free_number(map_log)
        for key in map_log:
            if key != free_number:
                for duration in map_log[key]:
                    payment += self.compute_price(duration)
        return payment

# class created for the call duration
class Duration:

    def __init__(self, hour, min, second):
        self.hour = hour
        self.min = min
        self.second = second

    def __repr__(self):
        time = ""
        return time + self.hour + ":" + self.min + ":" + self.second

    # call duration in seconds
    def duration_seconds(self):
        seconds = 0
        if self.hour != 0:
            seconds += int(self.hour) * 3600
        if self.min != 0:
            seconds += int(self.min) * 60
        seconds += int(self.second)
        return seconds


if __name__ == '__main__':
    input_test = "00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090"
    s = "00:01:07,400-234-090\n00:06:07,101-080-080\n00:05:00,400-234-090"
    test_2 = "00:02:07,401-234-090\n00:04:07,101-080-080\n00:06:00,400-234-090"
    test_3 = "00:00:00,401-234-090\n00:04:07,101-080-080\n00:06:00,400-234-090"
    solution = Solution()
    # duration = Duration(00, 06, 07)
    # print solution.compute_price(duration)
    # map_log = solution.parse_log(s)
    # print solution.free_number(map_log)
    print solution.solution(s)