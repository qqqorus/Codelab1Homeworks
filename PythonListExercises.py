#Python List Exercises

# 1. creating a list
favorite_fruits = ['banana', 'avocado', 'pineapple', 'mangosteen', 'mango']
print(favorite_fruits)

# 2. accessing elements
colors = ['red', 'blue', 'green', 'yellow', 'purple']
print("First color:", colors[0]) # print the first color
print("Third color:", colors[2]) # print the third color
print("Last color:", colors[-1]) # print the last color 

# 3. modifying a list
numbers = [10, 20, 30, 40, 50]
numbers[1] = 25 # change the second item to 25
numbers.append(60) # add 60 to the end of the list
print(numbers)

# 4. list slicing
names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
subset = names[0:3] # slices the first three names
print(subset)

# 5. looping through a list
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in list_of_numbers: 
    print(number ** 2) # print each number squared

# 6. list methods: append and extend
shopping_cart = []
# using .append() to add 'milk', 'bread', and 'eggs'
shopping_cart.append('milk')
shopping_cart.append('bread')
shopping_cart.append('eggs')
print(shopping_cart)
# using .extend to add ['butter', 'cheese'] to the list
shopping_cart.extend(['butter', 'cheese'])
print(shopping_cart)

# 7. finding maximum and minimum in a list
numbers = [45, 22, 88, 56, 92, 33] 
print(f"Maximum number:", max(numbers)) # finding the maximum number in the list
print(f"Minimum number:", min(numbers)) # finding the minimum number in the list

# 8. counting occurrences
letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
occurrences_of_a = letters.count('a') # count how many times the letter 'a' appears
print(f"There are {occurrences_of_a} occurrences of the letter 'a'.")

# 9. list comprehension
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# creates a new list which checks if the remainder of a number in the previous list is 0;
# and squares the numbers with a remainder of 0 also known as an even number 
numbers_squared = [number ** 2 for number in numbers if number % 2 == 0]
print(numbers_squared)

# 10. removing duplicates
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
for num in nums:
    if nums.count(num) == 2: # checks if there are duplicates in the list
        nums.remove(num) # removes the duplicates in the list
print(nums)
