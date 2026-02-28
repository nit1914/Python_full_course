# Day 13 - List

# Creating lists
#fruits = ["Apple", "Banana", "Grapes"]
# print(fruits)

# #Indexing
# print(fruits[0]) # Apple
# print(fruits[1]) # Banana
# print(fruits[2]) # Grapes
# print(fruits[-1]) # Grapes
# print(fruits[-2]) # Banana
# print(fruits[-3]) # Apple

# #Updating list
# fruits[1] = "Orange"
# print(fruits) # ['Apple', 'Orange', 'Grapes']

# # Adding new item to list
# fruits.append("Mango")
# print(fruits) # ['Apple', 'Orange', 'Grapes', 'Mango']
# fruits.insert(1, "Strawberry")
# print(fruits) # ['Apple', 'Strawberry', 'Orange', 'Grapes', 'Mango']

# # Removing item from list
# fruits.remove("Grapes")
# print(fruits) # ['Apple', 'Strawberry', 'Orange', 'Mango
# fruits.pop(2)
# print(fruits) # ['Apple', 'Strawberry', 'Mango']


# # Slicing list
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[0:5]) # [1, 2, 3, 4, 5]
# print(numbers[5:]) # [6, 7, 8, 9, 10]
# print(numbers[:5]) # [1, 2, 3, 4, 5]
# print(numbers[::2]) # [1, 3, 5, 7, 9]
# print(numbers[1::2]) # [2, 4, 6, 8, 10]     


# # Looping 
# for f in fruits:
#     print(f)

# Clean City names

# raw = ["mUMbai","DELhi","pune"]
# clean = []
# for c in raw:
#     clean.append(c.strip().title())
# print(clean) # ['Mumbai', 'Delhi', 'Pune']


# # Replace wrong spelling

# wrong = ["Kolkatta","Bengluru"]
# fixed = []
# for c in wrong:
#     c = c.replace("Kolkatta", "Kolkata").replace("Bengluru", "Bengaluru")
#     fixed.append(c) 
# print(fixed) # ['Kolkata', 'Bengaluru']


# # Extract years
# codes = ["Laptop-2024", "Phone-2023", "Tablet-2022"]
# years = []
# for c in codes:
#     years.append(c[-4:])
# print(years) # ['2024', '2023', '2022']