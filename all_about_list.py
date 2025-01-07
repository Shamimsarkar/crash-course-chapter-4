# Take an empty list

name_of_invited_people = []

# Insert people to the dinner list

name_of_invited_people.append("arif")
name_of_invited_people.append("monin")
name_of_invited_people.append("faruk")
# Published the dinner invited people list

print(f"{name_of_invited_people}")
# The person who can't add the dinner

print("faruk")

# So remove the person who can't add the dinner

name_of_invited_people.remove("faruk")
# Replace the person who add instead of who can't add
name_of_invited_people.append("habib")

# Print the new list

print(name_of_invited_people)

# Print the news that you got big table for dinner

print("I found a bigger table so I need three more people to add")

# Add new one to the list in first position

name_of_invited_people.insert(0, "Tuser")
# Print the new list

print(name_of_invited_people)

# Add another person at the middle position

name_of_invited_people.insert(2, "salam")

# Print the new list

print(name_of_invited_people)

# Add new person at the end

name_of_invited_people.append("osman")

# Print the new list
print(name_of_invited_people)

# Sorting the list
name_of_invited_people.sort()
print(name_of_invited_people)

# Your new dinner table have not arrived till now. so you need to remove person from list
print("Dinner table have not arrived till now. so you need to remove person from list")
# Remove last person from the list

remove_last_person = name_of_invited_people.pop(-1)

print(f"Sorry I can't in invite you this time {remove_last_person}")
# After removing last person
print(name_of_invited_people)

remove_last_person = name_of_invited_people.pop(-1)

print(f"Sorry I can't in invite you this time {remove_last_person}")

# After remove second last person from list

print(name_of_invited_people)

# Remove last person from the list

remove_last_person = name_of_invited_people.pop(-1)

print(f"Sorry I can't in invite you this time {remove_last_person}")
# After removing last person
print(name_of_invited_people)

# Remove last person from the list

remove_last_person = name_of_invited_people.pop(-1)

print(f"Sorry I can't in invite you this time {remove_last_person}")
# After removing last person
print(name_of_invited_people)

print(f"You are till invited: {name_of_invited_people[0]}")
print(f"You are till invited: {name_of_invited_people[1]}")

del name_of_invited_people[0]

print(name_of_invited_people)

del name_of_invited_people[0]

print(name_of_invited_people)




