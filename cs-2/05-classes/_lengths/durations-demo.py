class Duration:
    def __init__(self, hours, minutes):
        self.hours = hours + minutes // 60
        self.minutes = minutes % 60

    def __repr__(self):
        return f"{self.hours}h {self.minutes}m"


d = Duration(1, 30)

print(d)
print(d.hours)
print(d.minutes)

print(Duration(2, 0))
print(Duration(0, 160))


class LengthImperial:
    def __init__(self, feet, inches):
        self.feet = feet + inches // 12
        self.inches = inches % 12

    def __repr__(self):
        return f"{self.feet}'{self.inches}\""

    def to_metric(self):
        return LengthMetric((self.feet * 12 + self.inches) * 0.0254)


class LengthMetric:
    def __init__(self, meters):
        self.meters = meters

    def __repr__(self):
        return f"{round(self.meters, 2)}m"

    def to_imperial(self):
        return LengthImperial(0, self.meters * 39.3701)


li = LengthImperial(5, 7)

print(li)
print(li.feet)
print(li.inches)
print(li.to_metric())

print(LengthImperial(10, 0))
print(LengthImperial(0, 76))

lm = LengthMetric(1.93)

print(lm)
print(lm.meters)
print(lm.to_imperial())

print(LengthMetric(1000))
print(LengthMetric(4.567))
