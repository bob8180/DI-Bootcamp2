#1
# Ask the user for inputs
number = int(input("Enter a number: "))
length = int(input("Enter the length: "))

# Generate list of multiples
multiples = []

for i in range(1, length + 1):
    multiples.append(number * i)

# Print the result
print(f"\nThe list of multiples of {number} (length {length}):")
print(multiples)

#2
# Ask the user for input
text = input("Enter a string: ")

if text:  # check string is not empty
    result = text[0]  # Start with the first character
    
    for char in text[1:]:  # Loop through the string starting from the second character
        if char != result[-1]:   # only add if not same as last
            result += char
else:
    result = ""

# Print the modified string
print("Modified string:", result)