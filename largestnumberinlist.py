def find_largest_number(list):
# Initialize the first element as the largest
    largest = list[0]

# Loop through the list
    for i in list:
        if i > largest:  # Compare the value directly
            largest = i  # Update largenum if current number is larger
    return largest


# Print the largest number after the loop
list = [33,55,66,22,42]
largest_number = find_largest_number(list)
print(f"The largest number in the list is: {largest_number}")