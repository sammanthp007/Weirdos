meal_cost = float(input())
tip_percent = float(input())
tax_percent = float(input())

def get_total_cost(cost, tip, tax):
    tip = cost * (tip / 100.0)
    tax = cost * (tax / 100.0)
    total = cost + tip + tax
    return int(total + 0.5)

total = get_total_cost(meal_cost, tip_percent, tax_percent)

print ("The total meal cost is " + str(total) +" dollars.")
