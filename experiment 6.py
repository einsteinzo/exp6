def calculate_tax(income):
    brackets = [(11000, 0.10), (44725, 0.12), (95375, 0.22), (182100, 0.24), (231250, 0.32), (578125, 0.35), (float('inf'), 0.37)]
    tax, prev = 0, 0
    for limit, rate in brackets:
        if income > limit:
            tax += (limit - prev) * rate
            prev = limit
        else:
            tax += (income - prev) * rate
            break
    return round(tax, 2)

income = float(input("Enter your income: "))
print(f"Tax owed: ${calculate_tax(income)}")
