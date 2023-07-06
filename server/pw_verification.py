"""
This file is used to verify the password of the user.

The password is hashed and salted using the bcrypt library.

The password is hashed and salted when the user registers and is stored in the database.
"""

# import bcrypt


def verify_password(password, hashed_password):
    """
    This function is used to verify the password of the user.

    The password is hashed and salted using the bcrypt library.

    The password is hashed and salted when the user registers and is stored in the database.

    :param password: The password the user entered.
    :param hashed_password: The hashed and salted password stored in the database.
    :return: True if the password is correct, False if the password is incorrect.
    """
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))


def hash_password(password):
    """
    This function is used to hash and salt the password of the user.

    The password is hashed and salted using the bcrypt library.

    The password is hashed and salted when the user registers and is stored in the database.

    :param password: The password the user entered.
    :return: The hashed and salted password.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def main():
    """
    This function is used for testing purposes.
    """
    password = input("Enter a password: ")
    hashed_password = hash_password(password)
    print("Hashed password: " + hashed_password)
    password = input("Enter a password: ")
    print("Password is correct: " + str(verify_password(password, hashed_password)))


if __name__ == "__main__":
    main()
