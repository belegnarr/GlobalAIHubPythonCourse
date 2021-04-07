#Homework 2 _ Day-3

#Question 1
"""User login application: 
-Get Username and Password values from the user.
-Check the values in an if statement and tell the user if they were successful."""

username , password = "belegnarr" , "python123"
enter_username = input("User name: ")
enter_password = input("Password : ")

if enter_username == username and enter_password == password:
    print("Login successful.")
elif enter_username != username and enter_password == password:
    print("Wrong username!")
elif enter_username == username and enter_password != password:
    print("Wrong password!")
else:
    print("Login failed.")

#Extra:
"""-Try building the same user login application but this time, use a dictionary!"""

login_info = {"belegnarr":"python123","eregnarr":"4321"}
enter_username , enter_password= input("User name: ") , input("Password : ")

for u,p in login_info.items():
    if enter_username == u and enter_password == p:
        print("Login successful.")
if enter_username != u or enter_password != p:
    print("Login failed.")
