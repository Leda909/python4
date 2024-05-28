# Import haslib libary
import hashlib

# Welcome message!
print("Welcome to the Voting System!")

# Create an empty dictionary to store hashed votes. 
# Dictionary is an unordered collection of unique values stored in (key-value) pairs. d = {'a':1, 'b':2} = d['a'], d['b']
votes = {}

# Function to create the hashed_vote, with parameters of Name and Candidate ID
def hash_vote(name, candidate_id):
  # Hash the user's name combined with the candidate ID using SHA-256 algorithm
  hashed_vote = hashlib.sha256((name + str(candidate_id)).encode()).hexdigest()
  return hashed_vote

# Function to display the menu
def display_menu():
  print("\nPlease choose an option:") # \n = newLine
  print("1. Vote for a candidate")
  print("2. View voting results")
  print("3. Quit")

# Function to vote for a candidate
def vote():
  print("\nAvailable candidates:")
  print("1. Alice")
  print("2. Bob")
  print("3. Charlie")
  # Declare the two varible which will be used as parameters to create hashed_vote
  name = input("Enter your name: ")
  candidate_id = int(input("Enter the candidate ID you wish to vote for: "))
  # Call the hash_vote function with 'name' and 'candidate_id' as arguments/parameter and store the result in 'hashed_vote'
  hashed_vote = hash_vote(name, candidate_id)
  # Use 'hashed_vote' as the key and 'candidate_id' as the value to store the vote in the 'votes' dictionary
  votes[hashed_vote] = candidate_id
  print("Thank you for voting!")

# Function to view voting results
def view_results():
  print("\nVoting Results:")
  # Initialize a candidates dictionary to keep track of the vote counts for each candidate. Name is the key and value is the votes.
  candidates = {"Alice": 0, "Bob": 0, "Charlie": 0}
  # Iterate through each hashed_votes in the votes dictionary 
  for hashed_vote in votes:
    # Retrieve the candidate ID associated with the hashed vote
    candidate_id = votes[hashed_vote]
    # Increment the vote count for the corresponding candidate based on the candidate ID
    if candidate_id == 1:
      candidates["Alice"] += 1
    elif candidate_id == 2:
      candidates["Bob"] += 1
    elif candidate_id == 3:
      candidates["Charlie"] += 1
  # Iterate through the candidates dictionary to print out the vote counts for each candidate
  for candidate, count in candidates.items():
    # Print the candidate name and their respective vote count by f-string
    print(f"{candidate}: {count} votes")

# Main program, use while loop to run continously until the user quite
while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        vote()
    elif choice == "2":
        view_results()
    elif choice == "3":
        print("Thank you for using the Voting System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
