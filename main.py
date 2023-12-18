import os
import json

# Path details
directory_path = '/Users/amitdahan/logs'
file_name = 'moshe15-12-2023.log'
file_path = os.path.join(directory_path, file_name)

# Check if the directory exists
if os.path.exists(directory_path):
    # Get a list of all files and folders in the directory
    contents = os.listdir(directory_path)

    # Display the list of files in the directory
    print("Files in the directory:")
    for item in contents:
        item_path = os.path.join(directory_path, item)
        if os.path.isfile(item_path):
            print(item)
        else:
            print("The specified directory does not exist.")
print()

with open(file_path, 'r') as file:
    file_contents = file.read()

# Split the content into separate JSON objects
json_objects = file_contents.strip().split('\n\n')

# Keys to assert for JSON objects
keys_to_assert = ["id", "srv", "protyp", "@ver", "typ", "sens", "comm", "time", "host"]

# Process each JSON object separately
for obj in json_objects:
    try:
        json_data = json.loads(obj)

        # Check if 'sens' and 'protyp' exist and if 'sens' is '123' and 'protyp' is 'whatsapp'
        if 'sens' in json_data and 'protyp' in json_data and json_data['sens'] == '123' and json_data['protyp'] == 'whatsapp':
            # Check missing keys in the JSON object
            missing_keys = [key for key in keys_to_assert if key not in json_data]
            print(json.dumps(json_data, indent=2))  # Print the JSON object
            if missing_keys:
                print(f"The missing keys for type '{json_data.get('typ')}' are:")
                print(', '.join(missing_keys))  # Print the missing keys
            else:
                print("Nothing is missing.")
            print()  # Print an empty line for separation
    except json.JSONDecodeError:
        pass  # Ignore non-JSON lines
