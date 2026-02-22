# String Methods (Very Important)

# text = "    Data Analytics     "

# # Remove Spaces
# print("Original Text:", text)
# print("Remove Spaces:", text.strip())

# # Convert to Uppercase
# print("Uppercase:", text.upper().strip())

# # Convert to Proper case
# print("Proper Case:", text.strip().title())

# #Convert to lowercase
# print("Lowercase:", text.strip().lower())

# # #Replace
# print("Replace:", text.strip().replace("Data", "Business"))

# #Count Occurences
# print("Count Occurences of 'a':", text.count("a"))

# # Check if text starts with something
# print("Starts with 'Data':", text.strip().startswith("Data"))


# # Check if only numbers are present in data
# mobile = "9876543210"
# print("Is Mobile Number:", mobile.isdigit())

# #split string into the list of words
# msg = "Data Analytics is important"
# words = msg.split()
# print("Words list:", words)

# #join list of words into string
# joined_msg = "_".join(words)
# print("Joined Message:", joined_msg)

# #Find position of letter
# print("Position of 'a':", msg.find("a")) #first occurrence


# #Extract domain
# email="student@university.com"
# domain = email[email.find("@")+1:]
# print("Domain:", domain)
