# Bad
def process_users(users):
    for user in users:
        if user['active']:
            if user['age'] > 18:
                print(user['name'])

# Good
def is_active_adult(user):
    return user['active'] and user['age'] > 18

def process_users(users):
    for user in users:
        if is_active_adult(user):
            print(user['name'])
