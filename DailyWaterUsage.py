def shower_usage(minutes):
    return minutes * 9
def dishwasher_usage(cycles):
    return cycles * 12
def toilet_usage(flushes):
    return flushes * 6

showerUsage = shower_usage(float(input("How many minutes have you spent in the shower? ")))
dishwasherUsage = dishwasher_usage(int(input("How many dishwasher cycles have you used? ")))
toiletUsage = toilet_usage(int(input("How many times have you flushed the toilet? ")))

totalWaterUsage = showerUsage + dishwasherUsage + toiletUsage
print(f"You have used {totalWaterUsage} litres of water. ")