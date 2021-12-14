from datetime import datetime


def countAngle(hour, minute):
    angle = abs((hour%12)*30 - minute*6)
    return (min(angle, 360-angle))


def getAngle():
    time = datetime.now()
    return (countAngle(time.hour, time.minute))


def getDefinedAngle(time=None):
    hour, minute = map(int, time.split(':'))
    return (countAngle(hour, minute))
