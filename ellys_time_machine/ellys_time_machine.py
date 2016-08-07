class EllysTimeMachine(object):
    def getTime(self, time):
        s = ("12" if time[3:] == "00" else str(int(time[3:])/5).zfill(2)) + "%s" + str(int(time[:2])*5).zfill(2)
        conversion = s % ":"
        return conversion

if __name__ == '__main__':
    time = "01:00"
    elly = EllysTimeMachine()
    print elly.getTime(time)