import json
import os

FILE_NAME = "database2.0.json"

def load_profiles():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except:
        return []

def save_profiles(profiles):
    with open(FILE_NAME, "w") as f:
        json.dump(profiles, f, indent=2)

def add_profile(profiles):
    name = input("username: ").strip()

    for p in profiles:
        if p["name"].lower() == name.lower():
            print("profile already exists!")
            return  

    age = input("Age : ")
    city = input("City : ")

    new_profile = {"name": name, "age": age, "city": city}
    profiles.append(new_profile)
    save_profiles(profiles)
    print("Profile saved!")

def search_profile(profiles):
    search = input("Search name: ").lower().strip()
    found = False

    for p in profiles:
        if search in p["name"].lower():
            print(p)
            found = True

    if not found:
        print("profile doesn't found")

def main():
    profiles = load_profiles()
    while True:
        print("\n1. Add Profile\n2. Search Profile\n3. Show All\n4. Exit")
        choice = input("Choice: ")
        if choice == "1":
            add_profile(profiles)
        elif choice == "2":
            search_profile(profiles)
        elif choice == "3":
            print(profiles)
        elif choice == "4":
            break

main()