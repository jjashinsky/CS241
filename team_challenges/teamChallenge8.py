class Time:
    
    def __init__(self):
        self._seconds = 0
        self._minutes = 0
        self._hours = 0
    
    def _get_seconds(self):
        return self._seconds

    def _set_seconds(self, value):
        if value > 59:
            self._seconds = 59
        elif value < 0:
            self._seconds = 0
        else:
            self._seconds = value
    
    def _get_minutes(self):
        return self._minutes
    
    def _set_minutes(self, value):
        if value > 59:
            self._minutes = 59
        elif value < 0:
            self._minutes = 0
        else:
            self._minutes = value
    
    def _get_hours(self):
        return self._hours
    
    def _set_hours(self, value):
        if value > 23:
            self._hours = 23
        elif value < 0:
            self._hours = 0
        else:
            self._hours = value
            
    @property
    def hours(self):
        return self._get_hours()
    
    @hours.setter
    def hours(self, value):
        return self._set_hours(value)
    
    @property
    def minutes(self):
        return self._get_minutes()
    
    @minutes.setter
    def minutes(self, value):
        return self._set_minutes(value)
    
    @property
    def seconds(self):
        return self._get_seconds()
    
    @seconds.setter
    def seconds(self, value):
        return self._set_seconds(value)
            
    
            
def main():
    
    time = Time()

    value = float(input("Enter hour: "))
    time.hour = value
    
    value = float(input("Enter minutes: "))
    time.minutes = value
    
    value = float(input("Enter seconds: "))
    time.seconds = value
    
    print()

    print("The time is:")
    print("Hours: {}".format(time.hours))
    print("Minutes: {}".format(time.minutes))
    print("Seconds: {}".format(time.seconds))
   

if __name__ == "__main__":
    main()