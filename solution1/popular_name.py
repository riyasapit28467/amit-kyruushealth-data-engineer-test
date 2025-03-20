import os
from collections import defaultdict

start_year = int(input("Enter the start year: "))
end_year = int(input("Enter the end year: "))

def read_baby_name_data(directory, start_year, end_year):
    name_counts = {'M': defaultdict(int), 'F': defaultdict(int)}
    if start_year > end_year:
        raise ValueError("Start year must be less than or equal to end year.")

    for year in range(start_year, end_year + 1):
        year_file = f'yob{year}.txt'  
        file_path = os.path.join(directory, year_file) 

        try:
            with open(file_path, 'r') as f:
                for line in f:
                    name, gender, count = line.strip().split(',')
                    count = int(count)  
                    name_counts[gender][name] += count  
        except FileNotFoundError:
            print(f"File {file_path} does not exist.")
        except ValueError:
            print(f"Line format error in file {file_path}.")

    return name_counts  


def most_popular_names(directory, start_year, end_year):
    name_counts = read_baby_name_data(directory, start_year, end_year)
    most_popular = {}

    for gender, names in name_counts.items():
        if names:
            most_popular[gender] = max(names.items(), key=lambda item: item[1])

    return most_popular  


if __name__ == "__main__":
    # Example usage
    names_directory = 'names'  # Replace with your actual directory path
    
    most_popular = most_popular_names(names_directory, start_year, end_year)
    
    for gender, (name, count) in most_popular.items():
        print(f"{gender}:{name} with a count of {count}.")
    
    if not most_popular:
        print(f"No data found for the years {start_year} to {end_year}.")


# SQL

# SELECT 
#     gender,
#     name
# FROM baby_names
# WHERE year BETWEEN <start-year> AND <end-year>
# ORDER BY gender, count DESC
# LIMIT 1;