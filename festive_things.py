import random
import csv


with open("festive_things.csv") as festive_things:
    festive_lists = csv.reader(festive_things)
    option = random.randint(0,3)
    choice = random.choice(list(festive_lists))[option]
    print(choice)
