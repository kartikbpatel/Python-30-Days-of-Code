meal_cost  = float(input())
tip_percent = int(input())
tax_percent = int(input())

tip = float(meal_cost * tip_percent / 100)
tax = float(meal_cost * tax_percent / 100)
total = meal_cost + tip + tax
print ('The total meal cost is',round(total), 'dollars.') 