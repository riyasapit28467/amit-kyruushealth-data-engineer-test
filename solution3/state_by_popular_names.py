import json
import os

# Specify your input and output JSON file paths
input_file_path = 'input.json'
output_file_path = 'output.json'
states_directory = 'namesbystate'

def read_json(input_file_path):
    """Reads from the input JSON file and returns a list of all names."""
    with open(input_file_path, 'r') as file:
        data = json.load(file)
        names = []
        for unit in data['units']:
            names.extend(unit['names'])
        return names

def read_file_content_from_path(directory_path, names):
    """Reads the content of each file in the directory and returns the file names containing the specified names with the max count."""
    max_name_counts = {name: (None, 0) for name in names}  

    for filename in os.listdir(directory_path):
        if filename.endswith('.TXT'):
            name_counts = {name: 0 for name in names}
            with open(os.path.join(directory_path, filename), 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 5:
                        _, _, _, name, count = parts
                        count = int(count)
                        if name in names:
                            name_counts[name] += count
            for name, count in name_counts.items():
                if count > max_name_counts[name][1]:
                    max_name_counts[name] = (filename, count)

    return max_name_counts

def find_states_for_names(names, directory_path):
    """Finds the states for the given names based on the files in the directory."""
    state_data = {name: [] for name in names}

    for filename in os.listdir(directory_path):
        if filename.endswith('.TXT'):
            with open(os.path.join(directory_path, filename), 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 5:
                        state, _, _, name, _ = parts
                        if name in names:
                            state_data[name].append(state)

    return state_data

def create_output_data(input_data, directory_path):
    """Processes input data and returns formatted output data."""
    output = []

    for unit in input_data['units']:
        state_data = find_states_for_names(unit['names'], directory_path)
        max_name_counts = read_file_content_from_path(directory_path, unit['names'])
        unit_info = {
            "outputs": {name: {"State": file[0:2], "count": count} for name, (file, count) in max_name_counts.items()}
        }
        output.append(unit_info)

    return output

def write_json(output_file_path, data):
    """Writes data to the output JSON file."""
    with open(output_file_path, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    names = read_json(input_file_path)
    input_data = {'units': [{'name': 'unit1', 'names': names}]}
    output_data = create_output_data(input_data, states_directory)
    write_json(output_file_path, output_data)

    print(f"Output JSON written to {output_file_path}")

# Run the script
if __name__ == '__main__':
    main()
