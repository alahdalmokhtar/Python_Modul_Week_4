from datetime import datetime, timedelta
time_path='user.json'

import os
import json

if not os.path.exists(time_path):
    with open(time_path, 'w') as file:
        json.dump({}, file)


def read_json_file(file_path):
    """Read JSON file and return the data"""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
    
def save_time(user):
    """Save time to the JSON file"""
    with open(time_path, 'w') as file:
        json.dump(user, file,indent=4)

def load_time():
    if os.path.exists(time_path):
        with open(time_path, 'r', encoding='utf-8') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    else:
        return {}
     
def get_data(data):
    users = load_time()
    # Ensure users is a list
    if not isinstance(users, list):
        users = [users]
    # Add the new data
    #print("\n📦 Incoming data to save:")
    #print(json.dumps(data, indent=4, ensure_ascii=False))  # 
    users.append(data)
    save_time(users)
    print("✅ Data saved successfully.")

if __name__ == "__main__":
    main()

# Example usage.