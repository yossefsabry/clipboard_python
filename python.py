import sys
import clipboard
import json

SAVE_DATA = "clipboard.json"

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

def delete_data(filepath, key):
    data = load_data(filepath)
    if key in data:
        del data[key]
        save_data(filepath, data)
        print("Data deleted!")
    else:
        print("Key not found.")

if len(sys.argv) == 2:
    command = sys.argv[1]
    print(command)
    data = load_data(SAVE_DATA)

    # check for the command
    if command == "save":
        key = input("Enter a key to save : ")
        data[key] = clipboard.paste()
        save_data(SAVE_DATA, data)
        print("Data saved!")

    elif command == "load":
        key = input("Enter a key to load : ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("Key not found.")

    elif command == "list":
        print(data)

    elif command == "delete":
        key = input("Enter a key to delete: ")
        delete_data(SAVE_DATA, key)

    else:
        print("Unknown command")
else:
    print("Please enter one command.")