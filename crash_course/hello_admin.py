current_users = ['admin', 'mayo', 'Manolo', 'Fran', 'NAN', 'Marco']
new_users = ['Fran', 'NAN', 'Marco', 'silvia', 'mary']


current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())
print(current_users_lower)

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry " + new_user + ", that name is taken.")
    else:
        print("Great, " + new_user + " is still available.")
