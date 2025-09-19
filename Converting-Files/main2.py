# Slide 3 for Automation

import csv

def GetTargetCityIndex(targetCity:str, cities:list[str]) -> int:
    index:int = -1 # we will return -1 if the city is not found
    for i in range(len(cities)):
        if cities[i].lower() == targetCity.lower(): index = i
        # we can return from here, at the first index of city
        # or we can return after the loop completes, meaning
        # index will be equal to the LAST instance of city found
    return index

def ConvertCsv(csvPath:str, targetCity:str):
    data:list[str] = []
    with open(csvPath, "r") as csvFile:
        csvReader = csv.reader(csvFile)
        
        data = list(csvReader) # Convert the csv into a 2D list
    
    print(data[0]) # this will print out the cities
    print(data[0][2]) # this will print out the 2nd city (Portland)

    cities:str = data[0]
    cityIndex:int = GetTargetCityIndex(targetCity, cities)
    print(f"targetCity ({targetCity}) index is: {cityIndex}")


ConvertCsv("./temperature.csv", "Seattle")  