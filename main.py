#declearing class
class car:
    def __init__(self, gear, seats, maxspeed):
        self.gear = gear
        self.seats = seats
        self.maxspeed = maxspeed
    def speedup (self):
        print("speed increasing")
    def apply_break(self):
        print("speed decreasing")
class harrier (car):
    pass

c1 = car(5,3,200)
print(c1.gear)
