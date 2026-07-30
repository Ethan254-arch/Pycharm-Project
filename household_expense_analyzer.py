

with open('expenses.txt') as file:
    expenses = file.readlines()

    categories = []
    amounts = []

    category_amounts = []

    category_totals = {}

    for item in expenses:
        category = item.split(',')[0]
        amount = item.split(',')[1].strip('\n')

        categories.append(category)
        amounts.append(amount)

        category_amounts.append(f'{category}, {amount}')

    rent_total = 0
    groceries_total = 0
    transport_total = 0
    utilities_total = 0
    entertainment_total = 0

    for item in category_amounts:
        amount = float(item.split(',')[1])

        if item.startswith('Rent'):
            rent_total += amount
            category_totals["Rent Total"] = rent_total

        elif item.startswith('Groceries'):
            groceries_total += amount
            category_totals["Groceries Total"] = groceries_total

        elif item.startswith('Transport'):
            transport_total += amount
            category_totals["Transport Total"] = transport_total

        elif item.startswith('Utilities'):
            utilities_total += amount
            category_totals["Utilities Total"] = utilities_total

        elif item.startswith('Entertainment'):
            entertainment_total += amount
            category_totals["Entertainment Total"] = entertainment_total



    print(f"Category Totals Dictionary: {category_totals}")

    overall_expenditure = 0

    for item in category_totals:
        overall_expenditure += category_totals[item]

    print(f"Overall Expenditure: ${overall_expenditure}")

