#Task 2
airports = [
    ["BCN", "Barcelona International"],
    ["DUB", "Dublin"],
    ["LIS", "Lisbon"],
    ["LHR", "London Heathrow"],
    ["CDG", "Paris, Charles De Gaulle"],
    ["PRG", "Prague"],
    ["RKV", "Reykjavik"],
    ["FCO", "Rome, Fiumicino"]
]

def getAirportName(airportCode):
    for airport in airports:
        if airport[0].lower() == airportCode.lower():
            return airport[1]

print(getAirportName("FCO"))