import csv
import os

print(os.getcwd())
with open("./docs/sample.csv","r") as file:
    reader = csv.DictReader(file)
    counts = {}
    for line in reader:
        fav = line["Response"]
        print(fav)
        if fav in counts:
            counts[fav] += 1
        else:
            counts[fav] = 1


fav = input('Enter Fav ')

if fav in counts:
    print(f"{fav} : {counts[fav]}")



# def getValue(language):
#     return counts[language]


# for fav in sorted(counts, key=lambda language: counts[language], reverse=True):
#     print(f"{fav}: {counts[fav]}")
        
        

