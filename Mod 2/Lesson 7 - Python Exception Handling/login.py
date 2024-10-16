class UsernameError(Exception):
    pass

def check_username(username):
    try:
        if len(username) < 6:
            raise UsernameError
        else:
            print(f"{username} is valid.")
    except UsernameError:
        print(f"{username} is too short.")

username = input("Username?")
check_username(username)