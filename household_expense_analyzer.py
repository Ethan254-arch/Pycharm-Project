
import matplotlib.pyplot as plt

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


    for key, value in category_totals.items():
        if category_totals[key] == max(category_totals.values()):
            print(f"Highest Spending Category: {key.strip('Total')}")

    rent_amounts = []
    groceries_amounts = []
    transport_amounts = []
    utilities_amounts = []
    entertainment_amounts = []

    for item in category_amounts:
        amount = float(item.split(',')[1])

        if item.startswith('Rent'):
            rent_amounts.append(amount)
        elif item.startswith('Groceries'):
            groceries_amounts.append(amount)
        elif item.startswith('Transport'):
            transport_amounts.append(amount)
        elif item.startswith('Utilities'):
            utilities_amounts.append(amount)
        elif item.startswith('Entertainment'):
            entertainment_amounts.append(amount)

    plt.subplot(3, 2, 1)
    plt.plot(rent_amounts, 'r', label="Rent")
    plt.ylabel("Rent (USD)")

    plt.subplot(3, 2, 2)
    plt.plot(groceries_amounts, 'y', label="Groceries")
    plt.ylabel("Groceries (USD)")

    plt.subplot(3, 2, 3)
    plt.plot(transport_amounts, 'b', label="Transport")
    plt.ylabel("Transport (USD)")

    plt.subplot(3, 2, 4)
    plt.plot(utilities_amounts, 'g', label="Utilities")
    plt.ylabel("Utilities (USD)")

    plt.subplot(3, 2, 5)
    plt.plot(entertainment_amounts, 'm', label="Entertainment")
    plt.ylabel("Entertainment (USD)")

    plt.show()

    totals = []

    for item in category_totals.values():
        totals.append(item)



    sum=0

    for num in totals:
        sum += num
        percent_rent = f'{((totals[0] / sum) * 100):.2f}'
        percent_groceries = f'{((totals[1] / sum) * 100):.2f}'
        percent_transport = f'{((totals[2] / sum) * 100):.2f}'
        percent_utilities = f'{((totals[3] / sum) * 100):.2f}'
        percent_entertainment = f'{((totals[4] / sum) * 100):.2f}'



    labels = [f'Rent ({percent_rent}%)', f'Groceries ({percent_groceries}%)', f'Transport ({percent_transport}%)', f'Utilities ({percent_utilities}%)', f'Entertainment ({percent_entertainment}%)']



    plt.pie(totals, labels=labels)
    plt.title("Financial Summary Pie Chart")
    plt.show()