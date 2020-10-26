#This file will be responsible for displaying a quote in a fancy way
import tkinter as tk
import csv
import random


quotes = []

with open("quotes.csv", "r") as input_file:
    reader = csv.reader(input_file)
    for line in reader:
        quotes.append((line[0],line[1]))

#Tests import functionality of quotes
print(quotes[0][0])