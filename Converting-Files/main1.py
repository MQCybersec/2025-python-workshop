# Slide 2 for Automation

import csv

def ConvertCsv(csvPath):
    # "r" = read, "w" = write, "a" = append
    with open(csvPath, "r") as csvFile:
        csvReader = csv.reader(csvFile)
        for i in range(5):
            print(f"{csvReader.line_num}: {next(csvReader)}")

ConvertCsv("./temperature.csv")  