# Day-17 Range + Loops

# # Print 1 to 5
# for i in range (1,6):
#     print(i)

# # print Even Numbers(0-18)
# for i in range(0,20,2):
#     print(i)

# # Countdown from 10 to 1
# for i in range (10,0,-1):
#     print(i)

# #print Loop through list using index
# items = ["Pen","Book","Laptop"]
# for i in range (len(items)):
#     print(i,items[i])

# #Generate Employee IDs
# for i in range (1,6):
#     print("Emp-",i)

# # create years list
# years =[]
# for y in range(2015,2026):
#     years.append(y)
# print(years)


# # Clean city names using range
# cities = ["mUMbai","DELhi","pune"]
# for i in range (len(cities)):
#     cities[i] = cities[i].strip().title()
# print(cities)

# # Extract last 4 digits from IDs
# ids = ["EMP-001122","EMP-550044","EMP-990011"]
# for i in range (len(ids)):
#     print(ids[i][-4:])


# # Nested Loop
# for i in range(1,11):
#     for j in range (1,11):
#         print(f"i value : {i} J value : {j}")