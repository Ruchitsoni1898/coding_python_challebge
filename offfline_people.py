def offline_status(dictionary):
    count = 0
    for key in dictionary:
        if dictionary[key] == "offline":
            count+=1
    return count

statuses = {
   "alice": "online",
   "bob": "offline",
   "jack": "online",
  "maya": "offline",
  "sandra": "online"
}

print(offline_status(statuses))