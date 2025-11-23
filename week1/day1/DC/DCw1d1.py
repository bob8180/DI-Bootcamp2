# Ask for user input
user_str = input("Enter a string of exactly 10 characters: ")

# Step 2: Check length
if len(user_str) < 10:
    print("String not long enough.")
elif len(user_str) > 10:
    print("String too long.")
else:
    # Step 3: Valid length
    print("Perfect string")

    # Print first and last characters
    print("First character:", user_str[0])
    print("Last character:", user_str[-1])

    # Step 4: Build and print progressively
    print("\nBuilding string:")
    progressive = ""
    for char in user_str:
        progressive += char
        print(progressive)
