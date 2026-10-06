import json
import os

# Function to load all profiles safely
def load_all_profiles():
    # If file doesn't exist, return an empty list
    if not os.path.exists("database.json"):
        return []
    
    with open("database.json", "r") as file:
        return json.load(file)

# Task 1: Complete this function to save the updated list
def save_all_profiles(profile_list):
    with open("database.json", "w") as file:
        json.dump(profile_list, file, indent=4)
        pass

# --- Main Program Logic ---
profiles = load_all_profiles()

while True:
    print("\n--- 1. Add Profile | 2. View All | 3. Exit ---")
    choice = input("Enter choice (1/2/3): ")
    
    if choice == "1":
        name = input("Enter name: ")
        skill = input("Enter skill: ")
        
        # Create a new profile dictionary
        new_profile = {"name": name, "skill": skill}
        
        profiles.append(new_profile)
        
        # Save the updated list back to the file
        save_all_profiles(profiles)
        print("Profile added successfully!")
        
    elif choice == "2":
        print("\n--- All Registered Profiles ---")
        for p in profiles:
            print(p["name"])
        
    elif choice == "3":
        print("Goodbye!")
        break