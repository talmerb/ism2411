# Self-Assessment
#
# 1. In Exercise 5, the first bug I spotted was that total = sale was
# replacing the total every time through the loop instead of adding each
# sale to the total. I found the problem by tracing the values with print
# statements and looking through the loop. This showed me that I need to
# pay attention to how variables change during each loop instead of only
# looking at the final output.
#
# 2. apply_discount(price, tier) takes the original price and the customer's
# discount tier as inputs. It checks whether the tier is gold, silver,
# bronze, or none and applies the correct discount. It returns the price
# after the discount. A colleague could understand how to use the function
# without needing to read the body of it.
#
# 3. AI Disclosure:
# I used AI to help explain concepts and check my code during this lab.
# I used the explanations to help understand functions, loops, conditionals,
# debugging, and scope.


# --- Exercise 1 ---

def calculate_tax(price, rate):
    return price * rate


tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")


# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price


price = 200

print(f"gold: ${apply_discount(price, 'gold'):.2f}")
print(f"silver: ${apply_discount(price, 'silver'):.2f}")
print(f"bronze: ${apply_discount(price, 'bronze'):.2f}")
print(f"none: ${apply_discount(price, 'none'):.2f}")


# --- Exercise 3 ---

discounted_price = apply_discount(200, "gold")
tax = calculate_tax(discounted_price, 0.07)
after_tax = discounted_price + tax

print(f"After gold discount: ${discounted_price:.2f}")
print(f"After tax: ${after_tax:.2f}")


def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax


print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')


# --- Exercise 4 ---

orders = [
    (200, "gold"),
    (150, "silver"),
    (80, "bronze"),
    (500, "none")
]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5 ---

sales = [120, 80, 250, 175, 90]

# Bug 1:
# total = sale replaced the previous total on every loop.
# Fixed by using += to add each sale to the running total.
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

# Bug 2:
# The for loop was missing a colon after "for sale in sales".
# Fixed by adding the colon.
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

# Bug 3:
# The while loop used <=, which let i become equal to len(sales).
# That caused an attempt to access an index that does not exist.
# Fixed by changing <= to <.
i = 0
while i < len(sales):
    print(sales[i])
    i += 1


# --- Exercise 6 ---

x = 100


def double_it():
    x = 999
    return x * 2


print(x)
print(double_it())
print(x)

# Scope explanation:
# The x inside double_it() is local to that function. It is separate from
# the global x outside the function, so calling double_it() does not change
# the global x. The global x therefore remains 100.
