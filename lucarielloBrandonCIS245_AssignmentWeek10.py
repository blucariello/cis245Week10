import os
import csv

fileName = input("Enter the name of the .csv file you are creating: ")
fileNameExt = ".csv"
fileName = fileName + fileNameExt
dirName = input("Enter the directory you would like to save in: ")
path = dirName + fileName


dirCheck = os.path.exists(path)


eName = str(input("Enter your name: "))
eAddress = str(input("Enter your address: "))
eNumber = str(input("Enter your phone number: "))

c = csv.writer(open(fileName, "w"))

c.writerow([eName + eAddress + eNumber])

c.close()

cr = csv.reader(open(fileName, "r"))
