available_toppings = ['Cheese', 'Ham', 'Bacon', 'Olives']
requested_toppings = ['Cheese', 'French Fries', 'Bacon']

for requested_toppings in requested_toppings:
  if requested_toppings in available_toppings:
    print(f"Adding {requested_toppings}!")
  else:
    print(f"Sorry we dont have {requested_toppings}!")

print("\nFinished Making yout Pizza!!")