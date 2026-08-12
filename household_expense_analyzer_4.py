import math

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

    rent_amounts = []
    groceries_amounts = []
    transportation_amounts = []
    utilities_amounts = []
    entertainment_amounts = []

    for item in category_amounts:
        amount = float(item.split(',')[1])

        if item.startswith('Rent'):
            rent_total += amount
            rent_amounts.append(amount)
            category_totals["Rent Total"] = rent_total

        elif item.startswith('Groceries'):
            groceries_total += amount
            groceries_amounts.append(amount)
            category_totals["Groceries Total"] = groceries_total

        elif item.startswith('Transport'):
            transport_total += amount
            transportation_amounts.append(amount)
            category_totals["Transport Total"] = transport_total

        elif item.startswith('Utilities'):
            utilities_total += amount
            utilities_amounts.append(amount)
            category_totals["Utilities Total"] = utilities_total

        elif item.startswith('Entertainment'):
            entertainment_total += amount
            entertainment_amounts.append(amount)
            category_totals["Entertainment Total"] = entertainment_total



    print(f"Category Totals Dictionary: {category_totals}")

    overall_expenditure = 0

    for item in category_totals:
        overall_expenditure += category_totals[item]

    print(f"Overall Expenditure: ${overall_expenditure}")

    for key, value in category_totals.items():
        if category_totals[key] == max(category_totals.values()):
            print(f"Highest Spending Category: {key.strip('Total')}")


    print()

    rent_average = rent_total / len(rent_amounts)
    groceries_average = groceries_total / len(groceries_amounts)
    transportation_average = transport_total / len(transportation_amounts)
    utilities_average = utilities_total / len(utilities_amounts)
    entertainment_average = entertainment_total / len(entertainment_amounts)


    print("FINANCIAL SUMMARY:".center(50))
    print('-'.center(50,'-'))
    print('Internal Expenses:')
    print(f'{'Rent':<30} ${rent_total}')
    print(f'{'Utilities':<30} ${utilities_total}')
    print('-'.center(50,'-'))
    print(f'{'Total Internal Expenses':<30} ${rent_total + utilities_total}')

    print('-'.center(50,'-'))
    print('External Expenses:')
    print(f"{'Transportation':<30} ${transport_total}")
    print(f"{'Groceries':<30} ${groceries_total}")
    print(f"{'Entertainment':<30} ${entertainment_total}")
    print('-'.center(50,'-'))
    print(f"{'Total External Expenses':<30} ${transport_total + groceries_total + entertainment_total}")


