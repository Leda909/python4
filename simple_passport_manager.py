import hashlib

print("Welcome to our simple password manager!")

#Create an empty dictionary to store the usernames/passwords
passwords = {}

def hash_password(password):
  #Hash the password using SHA-256 algorithm
  hashed_password = hashlib.sha256(password.encode()).hexdigest()
  return hashed_password
  
#Asking the user to save usernames/passwords usiing the program
while True:
  website = input("Please enter a website/application you want to store a password for:")
  password = input(f"Please enter the password for {website}")
  secure_password = hash_password(password)
  passwords[website] = secure_password
  print("Password saved successfully!")
  
  another = input("Do you want to save another website/password? [YES/NO]")
  if another.lower() == 'no':
    print("Thank you!")
    break
  
#Ask the user to check if what they have entered is the password they have saved
while True:
  website_to_check = input("Please enter a website/application you want to check:")
  if website_to_check in passwords:
    entered_password = input(f"Please enter your password for {website_to_check}")
    secure_entered_password = hash_password(entered_password)
    if passwords[website_to_check] == secure_entered_password:
      print("Password is correct!")
    else:
      print("Incorrect password")
  else:
      print("No password stored for that website/application")
      
  another = input("Do you want to check another website")
  if another.lower() == 'no':
    print("Thank you!")
    break
