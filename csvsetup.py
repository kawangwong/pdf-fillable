import csv
from lazyfill import columns

# print(columns)
print(columns[0])


# item = columns[0]
# print(item)

with open("inputcsv.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(zip(columns))

print("complete")

