# Reflection
# 1. The most surprising feature of Python lists is that negative indices
#    let me access items from the end without calculating their positions.
#    Slices also make it easy to select several items at once, while methods
#    such as append() and sort() change the existing list.
#
# 2. In a business class, a list could help process daily sales figures for
#    a store by calculating totals, averages, and days above a target.
#    Instead of manually selecting Excel cells and repeating those steps
#    for each new report, I could reuse the same Python code with new data.


# Exercise 1: Build the list.
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print("Exercise 1")
print(inventory)
print(len(inventory))


# Exercise 2: Use positive and negative indices; compute the middle index.
print("\nExercise 2")
print(inventory[0])
print(inventory[-1])
middle_index = len(inventory) // 2
print(inventory[middle_index])


# Exercise 3: Slice the list.
print("\nExercise 3")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])


# Exercise 4: Modify the list and print after each operation.
print("\nExercise 4")
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)


# Exercise 5: Catch an attempt to change an immutable tuple.
print("\nExercise 5")
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples are useful for coordinates because their values cannot be changed accidentally.")
print(coords)


# Exercise 6: Summarize daily sales.
print("\nExercise 6")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")


# Exercise 7: Build a new list with an accumulator loop.
print("\nExercise 7")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.90, 2))
print(f"Original: {prices}")
print(f"Discounted: {discounted}")


# Exercise 8: Filter sales strictly above 300 and average the results.
print("\nExercise 8")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for sale in sales:
    if sale > 300:
        high_sales.append(sale)
print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Avg: {sum(high_sales) / len(high_sales):.2f}")
