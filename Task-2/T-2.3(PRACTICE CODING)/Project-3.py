print("login validation system: ")
user="admin"
passwrd="1234"
username=input("enter your username :").lower().strip()
password=input("enter your password :").lower().strip()

def login_validate(n,p):
     if n==user and p==passwrd:
      print("login successful")
     elif n=="" or p=="":
          print("you have enter empty password or username")
     else:
          print("Invalid credentials")
          

    
login_validate(username,password)

     