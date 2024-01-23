import csv

def checkPersonID(id):
    with open('trying/database.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['id'] == id:
                return row
    return None

def validate(id, password):
    user = checkPersonID(id)
    if user and user['password'] == password:
        return user
    return None

def renderLandingPage(user):
    print(f"Welcome, {user['username']}!")

def renderFeedAndNotifications(user):
    print(f"Posts: {user['posts']}")
    print(f"Notifications: {user['notifications']}")

def main():
    while True:
        id = input("Enter your ID: ")
        password = input("Enter your password: ")
        user = validate(id, password)
        if user:
            renderLandingPage(user)
            renderFeedAndNotifications(user)
            break
        else:
            print("Invalid ID or password.")

if __name__ == "__main__":
    main()