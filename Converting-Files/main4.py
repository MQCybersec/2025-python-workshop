# Slide 5 for Automation

import csv, json

def GetTargetCityIndex(targetCity:str, cities:list[str]) -> int:
    index:int = -1 # we will return -1 if the city is not found
    for i in range(len(cities)):
        if cities[i].lower() == targetCity.lower(): index = i
    return index

def DataFromRow(row, timeIndex, cityIndex):
    temperature = row[cityIndex]
    value = {
    "time": row[timeIndex].split(" ")[1], 
    "temperature": temperature
    }
    
    return value
    

def ConvertCsv(csvPath:str, targetCity:str):
    data:list[str] = []
    with open(csvPath, "r") as csvFile:
        csvReader = csv.reader(csvFile)
        data = list(csvReader) # Convert the csv into a 2D list
    cities:str = data[0]
    cityIndex:int = GetTargetCityIndex(targetCity, cities)
    timeIndex:int = 0 # time is always the first index of each row
    
    print(f"targetCity ({targetCity}) index is: {cityIndex}")

    dataForCity:dict = {} 
    dataForDay:list = []
    lastDate = ""
    for row in data:
        if len(row[timeIndex]) > 8 and len(row[cityIndex]) > 0: # filter out "datetime" as its 8 characters
            dateKey = row[timeIndex].split(" ")[0] # split at the space
            if lastDate == "": lastDate = dateKey # this is to stop an empty log for the first date
            if (dateKey != lastDate): # reset dataForDay if new day
                dataForCity[dateKey] = dataForDay
                dataForDay = []    
                lastDate = dateKey
            
            rowData = DataFromRow(row, timeIndex, cityIndex)
            dataForDay.append(rowData)
            

            input("-") # press enter to iterate through each row
            print(dataForDay) # should see dictionary grow until next day starts, where it resets

ConvertCsv("./temperature.csv", "Seattle")  