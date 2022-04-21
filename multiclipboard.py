import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

def saveData(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def loadData(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

#save data to clipboard (like copy)
# clipboard.copy("Whatever you want to copy")

# paste data from the clipboard
# data = clipboard.paste()
# print(data)

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = loadData(SAVED_DATA)

    if command == "save":
        key = input("Enter a Key: ")
        data[key] = clipboard.paste()
        saveData(SAVED_DATA, data)
        print("Data saved")

    elif command == "load":
        key = input("Enter a Key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard")
        else:
            print("The key does not exist")

    elif command == "list":
        print(data)

    else:
        print("Unknown Command")

else:
    print("Please use exactly 2 arguments")
