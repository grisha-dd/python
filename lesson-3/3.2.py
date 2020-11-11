def user_info(**kwargs):
    for key, value in kwargs.items():
        print("{} is {}. ".format(key, value), end="")


user_info(Firstname=input("Firstname: "), Lastname=input("Lastname: "), Birthyear=input("Birthyear: "),
          City=input("City: "), Email=input("Email: "), Phone=input("Phone: "))
