import pandas as pd

#pd.set_option('display.max_columns', None)

#pd.set_option('display.width', None)

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



    internal_expenses = pd.DataFrame(
        data = [rent_amounts,
                utilities_amounts],
        index = ['Rent', 'Utilities'],

    )

    internal_expenses.fillna(value=0, inplace=True)

    internal_expenses[20] = [rent_total, utilities_total]

    internal_expenses.rename(columns={20: 'Totals'}, inplace=True)

    print()
    print("Financial Summary:")

    print("Internal Expenses:")

    print(internal_expenses)

    external_expenses = pd.DataFrame(
        data = [groceries_amounts,
                transportation_amounts,
                entertainment_amounts],
        index = ['Groceries', 'Transport', 'Entertainment'],
    )

    external_expenses.fillna(value=0, inplace=True)

    external_expenses[30] = [groceries_total, transport_total, entertainment_total]

    external_expenses.rename(columns={30: 'Totals'}, inplace=True)

    print("External Expenses:")

    print(external_expenses)