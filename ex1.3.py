class TrafficManagementAgent:
    def __init__(self, congestion_threshold):
        self.congestion_threshold = congestion_threshold

    def control_traffic_light(self, traffic_density):
        if traffic_density > self.congestion_threshold:
            return "Extend Green Light Duration"
        else:
            return "Normal Traffic Light Cycle"

# Example usage
agent = TrafficManagementAgent(congestion_threshold=50)  # Threshold set at 50 vehicles

traffic_density = int(input("Enter current traffic density (number of vehicles): "))
action = agent.control_traffic_light(traffic_density)
print(action)

