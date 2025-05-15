import json
import requests
from operations import create_entry, update_entry, delete_entry

# Take API URL input from the user
print(f"""
      -----------Welcome to API operator----------
      Choose the operation you want to be executed:
      1. Create
      2. Update
      3. Delete
      """)
choice = int(input("Enter choice: "))
api_url = input("Enter the API URL: ").strip()

# Read payload from JSON file
try:
    with open('payload.json', 'r') as file:
        payload = json.load(file)

    headers = {
        "Content-Type": "application/json",
        # "Authorization": "Bearer YOUR_ACCESS_TOKEN"  # Optional
    }

    for pl in payload:
        print(pl)
        if choice == 1:
            response = create_entry(api_url=api_url, json=pl, headers=headers)
        elif choice == 2:
            response = update_entry(
                api_url=api_url, id=pl['id'], json=pl, headers=headers)
        elif choice == 3:
            response = delete_entry(
                api_url=api_url, id=pl['id'])
        else:
            print('Invalid Choice')
            break

        if response.status_code in [200, 201]:
            print("Success:", response.json())
        else:
            print("-------------------------Error------------------------\n", response.status_code, response.text)

except FileNotFoundError:
    print("payload.json not found.")
except json.JSONDecodeError:
    print("Invalid JSON in payload.json.")
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
