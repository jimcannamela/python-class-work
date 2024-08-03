import csv

with open('party.csv', 'r') as file:
    reader = csv.reader(file)
    party = list(reader)

print(party)