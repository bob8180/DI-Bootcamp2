#1
my_fav_numbers = {2,5,8,}
my_fav_numbers.add(33)
my_fav_numbers.add(38)
print(my_fav_numbers)
friend_fav_numbers = {3,17,25}
our_fav_numbers = friend_fav_numbers.union(my_fav_numbers)
print(our_fav_numbers)
#2
my_tuple = (1,3,5)
# my_tuple.add(4)
# AttributeError: 'tuple' object has no attribute 'add'
# PS C:\Users\BOB\Downloads\Data Analysis\Bootcamp25\Di-bootcamp>

#3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove('Banana')
basket.pop()
basket.append('Kiwi')
basket.insert(0,'Apples')
print(basket.count('Apples'))
print(basket)
basket.clear()
print(basket)

#4
my_list = []
my_item = 1
while my_item < 5:
    my_item += 0.5
    my_list.append(my_item)
print(my_list)

#5
print(list(range(1,21)))

for i in range(1, 21):
    if i % 2 == 0:   # check if number is even
        print(i)

#6
user_name = ""
while user_name == "":
    user_name = input("Please, enter your name.")
print(f'Your name is {user_name}')

#7
fav_fruits = input("Enter favorite fruits (you can input several fruits, separated by spaces).")
lst_fruits = fav_fruits.split()
fav_fruits = input("Enter the most favorite fruit.")
if fav_fruits in lst_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

#8
toppings = []

# Loop to collect toppings
while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")
    
    if topping.lower() == "quit":
        break
    
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

# Calculate total cost
base_price = 10
topping_price = 2.50
total_cost = base_price + topping_price * len(toppings)

# Print summary
print("\nYour pizza order summary:")
print("Toppings:", ", ".join(toppings) if toppings else "No extra toppings")
print(f"Total cost: ${total_cost:.2f}")

#9
total_cost = 0

while True:
    age_input = input("Enter the person's age (or type 'done' to finish): ")
    
    if age_input.lower() == "done":
        break
    
    # Convert to integer
    age = int(age_input)
    
    # Apply ticket price rules
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15
    
    total_cost += price

# Print total
print(f"\nThe total cost for the tickets is: ${total_cost}")

#10
# Initial list of sandwich orders
sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]

finished_sandwiches = []

print("Sorry, the deli has run out of Pastrami.\n")

# Remove all instances of "Pastrami"
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

# Prepare sandwiches
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)   # take the first order
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

# Final result
print("\nAll finished sandwiches:")
print(finished_sandwiches)