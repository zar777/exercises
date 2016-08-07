class EllysTimeMachine(object):
    def getTime(self, time):
        minutes = int(time[:2])*5 if int(time[:2])*5 != 60 else 00
        hours = (12 if time[3:] == "00" else int(time[3:])/5)
        if int(time[:2])*5 == 60:
            if hours == 12:
                hours = 1
            else:
                hours += 1
        s = str(hours).zfill(2) + "%s" + str(minutes).zfill(2)
        conversion = s % ":"
        return conversion

if __name__ == '__main__':
    time = "12:25"
    elly = EllysTimeMachine()
    print elly.getTime(time)