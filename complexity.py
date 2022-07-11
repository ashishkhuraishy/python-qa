# package to check regex
import re

def check_password(password):
    """
    A password is considered strong if:
        8 characters length or more
        1 digit or more
        1 symbol or more
        1 uppercase letter or more
        1 lowercase letter or more
    """

    # calculating the length
    if len(password) < 8:
        print("password should be atleast 8 digits")

    # searching for digits
    elif re.search(r"\d", password) is None:
        print("password should contain numbers")

    # searching for uppercase
    elif re.search(r"[A-Z]", password) is None:
        print("password should contain capital letters")

    # searching for lowercase
    elif re.search(r"[a-z]", password) is None:
        print("password should contain lowercase letters")
    
    # searching for charecters
    elif re.search(r"[ @!#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None:
        print("password should contain characters")

    # all the conditions are satisfied and the password is strong
    else:
        print("you have a strong password :)")


password = input("please enter your password : ")
check_password(password)