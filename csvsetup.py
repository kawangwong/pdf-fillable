import csv
from lazyfill import columns

print(columns)

with open("inputcsv.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(columns)

print("complete")

