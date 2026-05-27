print("login validation system")
username=input("enter your username: ")
password=input("enter your password: ")
if username=="admin" and password=="admin123":
    print("login successful")
elif username=="admin" and password!="admin123":
    print("invalid password")
elif username!="admin" and password=="admin123":
    print("invalid username")
else:
    print("login failed please enter valid username and password")
    