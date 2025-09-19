# Slide 4 for Automation

import csv

def GetTargetCityIndex(targetCity:str, cities:list[str]) -> int:
    index:int = -1 # we will return -1 if the city is not found
    for i in range(len(cities)):
        if cities[i].lower() == targetCity.lower(): index = i
    return index

def ConvertCsv(csvPath:str, targetCity:str):
    data:list[str] = []
    with open(csvPath, "r") as csvFile:
        csvReader = csv.reader(csvFile)
        data = list(csvReader) # Convert the csv into a 2D list
    cities:str = data[0]
    cityIndex:int = GetTargetCityIndex(targetCity, cities)
    timeIndex:int = 0 # time is always the first index of each row
    
    print(f"targetCity ({targetCity}) index is: {cityIndex}")

    for row in data:
        print(f"{row[timeIndex]}: {row[cityIndex]}")
        input("-") # press enter to iterate through each row

ConvertCsv("./temperature.csv", "Seattle")  