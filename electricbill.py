kw_hours = int(input("Enter the KW hours used: "))
if kw_hours > 1000:
    first_rate = 1000 * 7.633
    extra_hours = kw_hours - 1000
    extra_rate = extra_hours * 9.259
    total = (first_rate + extra_rate) / 100
else:
    total = (kw_hours * 7.633) / 100

print(f"Amount owed is ${total}")