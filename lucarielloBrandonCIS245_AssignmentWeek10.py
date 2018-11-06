import os
import csv

fileName = input("Enter the name of the .csv file you are creating: ")
fileNameExt = ".csv"
fileName = fileName + fileNameExt
dirName = input("Enter the directory you would like to save in: ")
path = dirName + fileName


dirCheck = os.path.exists(path)


eName = input("Enter your name: ")
eAddress = input("Enter your address: ")
eNumber = input("Enter your phone number: ")
  
c = csv.writer(open(fileName, "wb"))

c.writerow(eName + eAddress + eNumber)
