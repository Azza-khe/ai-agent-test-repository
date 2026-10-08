users = []


def add_user(name, email):
    user = {
        "name": name,
        "email": email
    }

    users.append(user)

    return user


def find_user(email):

    for user in users:

        if user["email"] == email:
            return user

    return None


def delete_user(email):

    for user in users:

        if user["email"] == email:
            users.remove(user)
            return True

    return False