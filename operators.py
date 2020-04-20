def solve(meal_cost, tip_percent, tax_percent):
    tip_cost = (tip_percent/100) * meal_cost
    tax_cost = (tax_percent/100) * meal_cost
    total_cost = int(round(meal_cost + tip_cost + tax_cost))
    print(total_cost)


print(solve(12.00, 20, 8))