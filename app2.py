import pyrebase

config = {
  "apiKey": "AIzaSyDZ4GU0X0KznmK3gCx8mVQqwZFjHKi46jE",
  "authDomain": "first-flask-app-7b882.firebaseapp.com",
  "projectId": "first-flask-app-7b882",
  "storageBucket": "first-flask-app-7b882.appspot.com",
  "messagingSenderId": "297760772258",
 "appId": "1:297760772258:web:8b4e08199b6571226f07fb",
  "measurementId": "G-NC80NQW7C2",
  "databaseURL": "https://first-flask-app-7b882-default-rtdb.firebaseio.com/"
}

firebase=pyrebase.initialize_app(config)
auth=firebase.auth()

def signup():
  print("Signup ")
  email = input("Enter email")
  password = input("password")
  try:
       user=auth.create_user_with_email_and_password(email,password)
       print("Successfully created")
       ask=input("Do you want to login now?[yes/no]")
       if ask=="yes":
         login()
  except:
    print("Email already exists")
    
    
def login():
  print("Login")
  email = input("Enter email")
  password = input("password")
  try:
   login=auth.sign_in_with_email_and_password(email,password)
   print("Successfully logged in")
   print(auth.get_account_info(login["idToken"]))
  except:
    print("Invalid email or password")
  
ans = input("Are you a new user:")
if ans=="yes":
   signup()
elif ans=="no":
   login()
  




  