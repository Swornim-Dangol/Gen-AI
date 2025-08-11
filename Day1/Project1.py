#inventory system 
import json 
import datetime

with open('items.json', 'r') as f:
        data = json.load(f)

def user_credentials():
    username = input("Enter your username: ")
    return username

def select_department():
    dept_map = {k.lower(): k for k in data.keys()}
    #check for department, if its not on the json file ask again 
    while True:
        print("Available departments: Electronics, Books, Clothing, Furniture")
        department = input("Enter the department you want to access: ")
        
        dept_key = department.lower()
        if dept_key not in dept_map:
            print(f"Error: Department '{department}' not found.")
            continue
        break

    actual_department = data[dept_map[dept_key]]
    print("Available items:")
    for item in actual_department:
        print(f"{item}: Price: {actual_department[item]['price']}, Count: {actual_department[item]['count']}")
    return dept_map[dept_key]

def select_item(department):
    #select item and if not in the json file ask again
    while True:
        item = input("Enter the item you want to select: ")
        if item not in data[department]:
            print(f"Error: Item '{item}' not found in department '{department}'.")
            continue
        break

    total = int(input("How many do you want to purchase? :"))
    return item,total

def puchase_item(user,department, item, total):
    #pouchase if available and log the purchase
    if data[department][item]['count'] < total:
        print(f"Error: Item '{item}' is out of stock.")
        return False
    data[department][item]['count'] -= total
    print(f"Purchased {item} from {department}. Remaining count: {data[department][item]['count']}")

    with open('items.json', 'w') as f:
        json.dump(data, f, indent=4)

    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('log.txt', 'a') as log_file:
        log_file.write(f"User:{user} has purchased {total} {item} at {time}\n")
    return True

user = user_credentials()
department = select_department()
item,total = select_item(department)
if puchase_item(user, department, item,total):
    print(f"Thank you for your purchase, {user}!")