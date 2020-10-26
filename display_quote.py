#This file will be responsible for displaying a quote in a fancy way
import tkinter as tk
import csv
import random


quotes = []
count = 0

with open("quotes.csv", "r") as input_file:
    reader = csv.reader(input_file)
    for line in reader:
        quotes.append((line[0],line[1]))
        count += 1

#Tests import functionality of quotes
#print(quotes[0][0])

#Generate random number in range of number of quotes
random_number = random.randrange(0, count)

#Assign the quote and author to their respective variables
quote = quotes[random_number][0]
author = quotes[random_number][1]

#Remove ending period, if there is one

if quote[-1] == ".":
    quote = quote[:-1]
print(quote + " - " + author)