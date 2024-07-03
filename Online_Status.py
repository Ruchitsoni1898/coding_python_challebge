def online_people(dictionary):
    count = 0
    for key in dictionary:
        if dictionary[key] == "online":
            count += 1
    return count

# statuses dictionary display
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Charlie": "online",
    "David": "offline",
    "Eve": "online"
}

# Calling the function and printing the statuses
print(online_people(statuses))
