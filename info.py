import json

info = [
    {"name": "Saksham", "Class": 5},
    {"skills": ["python", "astronomy", "edit", "ai prompting", "binary"]},
    {"dream": "software developer"},
    {"teacher": "Claude AI"}
]

with open("myself.json", "w") as file:
    json.dump(info, file, indent=4)