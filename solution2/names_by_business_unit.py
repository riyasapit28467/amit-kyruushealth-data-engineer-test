import json
import os
from collections import defaultdict

def read_business_units(file_path):
    with open(file_path, 'r') as json_file:
        return json.load(json_file).get("input", [])

def read_names_from_state(state):
    state_file_path = os.path.join('namesbystate', f'{state}.TXT')
    
    try:
        with open(state_file_path, 'r') as state_file:
            content = state_file.read().strip()
            names = content.splitlines()
            male_names_count = defaultdict(int)
            female_names_count = defaultdict(int)

            for line in names:
                parts = line.split(',')
                if len(parts) == 5:  # Ensure line has 5 parts as expected
                    gender = parts[1].strip()  # Gender is in the second place
                    name = parts[3].strip()    # Name is in the fourth place
                    count = int(parts[4].strip())  # Occurrence is in the fifth place

                    if gender == 'M':
                        male_names_count[name] += count  # Count male names by occurrences
                    elif gender == 'F':
                        female_names_count[name] += count  # Count female names by occurrences
            
            # Fetch most common names
            most_common_male = max(male_names_count.items(), key=lambda x: x[1], default=(None, 0))
            most_common_female = max(female_names_count.items(), key=lambda x: x[1], default=(None, 0))

            return {
                "Male": most_common_male[0],     # Name
                "Female": most_common_female[0]  # Name
            }
    except FileNotFoundError:
        print(f"State file {state_file_path} not found.")
        return None
    except Exception as e:
        print(f"Error reading file {state_file_path}: {e}")
        return None

# Function to create the output structure
def create_output(input_data):
    output = []
    
    for business_unit in input_data:
        name = business_unit['name']
        states = business_unit['states']
        
        # Initialize a dictionary for the business unit
        unit_info = {'name': name}

        # Aggregate names based on the states
        male_names = []
        female_names = []
        
        for state in states:
            names = read_names_from_state(state)
            if names:
                # Collect names if they exist
                if names['Male']:
                    male_names.append(names['Male'])  
                if names['Female']:
                    female_names.append(names['Female'])

        # Take the most common names overall for the business unit
        if male_names:
            unit_info["Male"] = max(set(male_names), key=male_names.count)
        if female_names:
            unit_info["Female"] = max(set(female_names), key=female_names.count)

        # Append the unit info to the output list
        output.append(unit_info)
    
    return {"output": output}

# Main function to orchestrate reading and writing JSON
def main():
    input_file_path = 'input.json'
    
    business_units = read_business_units(input_file_path)  # Read business units

    output_data = create_output(business_units)  # Create output data structure

    # Write the output data to a JSON file
    with open('output.json', 'w') as output_file:
        json.dump(output_data, output_file, indent=4)  # Write with pretty printing

    print("Output written to output.json")

# Run the main function
if __name__ == '__main__':
    main()