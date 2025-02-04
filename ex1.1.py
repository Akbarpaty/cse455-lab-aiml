class Roomheater:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def control_temperature(self, temp):
        if temp < self.min:
            return "heater on"
        elif temp > self.max:
            return "cooler on"
        else:
            return "Normal temp"


agent = Roomheater(min=20, max=25)

now_temp = float(input("enter temperature of room: "))
action = agent.control_temperature(now_temp)
print(action)
