costs = {
    "London": {
        "Dublin": 90,
        "Paris": 650
    },
    "Dublin": {
        "London": 90,
        "Reykjavik": 260,
        "Lisbon": 300
    },
    "Reykjavik": {
        "Dublin": 260,
        "Prague": 190
    },
    "Prague": {
        "Reykjavik": 190,
        "Rome": 150,
        "Paris": 100
    },
    "Rome": {
        "Prague": 150,
        "Paris": 210
    },
    "Barcelona": {
        "Lisbon": 110,
        "Paris": 100
    },
    "Lisbon": {
        "Dublin": 300,
        "Paris": 200,
        "Barcelona": 110
    },
    "Paris": {
        "London": 650,
        "Prague": 100,
        "Lisbon": 200,
        "Barcelona": 100,
        "Rome": 210
    }
}

def tripCost(city1, city2):
    return costs[city1][city2]
    
def getCostOfTrip(*cities):
    totalCost = 0
    lastCity = 0
    for i in range(1, len(cities)):
        totalCost += tripCost(cities[lastCity], cities[i])
        lastCity += 1
    return totalCost

print(getCostOfTrip("Dublin", "London", "Paris", "Rome"))
print(getCostOfTrip("Reykjavik", "Prague", "Rome", "Paris"))