# Day 20 |File Handling|


# # 1) Reading full file
# with open("day20_samples.txt","r") as f:
#     print(f.read())


# # 2) Reading line by line
# with open("day20_samples.txt", "r") as f:
#     for line in f:
#         print(line.strip().title())



# # 3) Writing (overwrite)
# with open("day20_notes.txt", "w") as f:
#     f.write("Day 20 - File Handling\n")
#     f.write("Learning read and write.\n")



# # # 4) Appending
# with open("day20_notes.txt", "a") as f:
#     f.write("Appending new line.\n")




# # 5) Cleaning data in file
# cleaned = []
# with open("day20_samples.txt", "r") as f:
#     for line in f:
#         cleaned.append(line.strip().title())  
# with open("day20_cleaned_output.txt", "w") as f:
#     for city in cleaned:
#         f.write(city + "\n")



# # 6) Counting lines
# count = 0
# with open("day20_samples.txt", "r") as f:
#     for _ in f:
#         count += 1
# print("Total Lines:", count)
 




