from datetime import datetime

currentTime = "2020-11-17"
separate = datetime.strptime(currentTime,"%Y-%m-%d")
print(separate)

print("Month: ", separate.month)
print("Day: ", separate.day)
print("Year:", separate.year)

dates = ["2020-11-17", "2020-01-16", "2020-07-15","2020-07-01"]

month_list = []
month_set = set()

for x in dates:
    print(x)
    print(x in dates)
    independent = datetime.strptime( x ,"%Y-%m-%d")
    print(independent)
    month_list.append(independent.month)
    month_set.add(independent.month)

print(month_list)
print(month_set)

