from calculator import divide
from user_service import add_user
from database import create_table


def main():

    create_table()

    user = add_user(
        "Azza",
        "azza@example.com"
    )

    print("User created:")
    print(user)

    result = divide(10, 2)

    print("Result:")
    print(result)


if __name__ == "__main__":
    main()