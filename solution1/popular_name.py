import os
from collections import defaultdict

start_year = int(input("Enter the start year: "))
end_year = int(input("Enter the end year: "))

def read_baby_name_data(directory, start_year, end_year):
    name_counts = defaultdict(int)
    if start_year > end_year:
        raise ValueError("Start year must be less than or equal to end year.")
    for year in range(start_year, end_year + 1):
        year_file = f'yob{year}.txt'  # Constructing the filename
        file_path = os.path.join(directory, year_file)  # Full path to the file
        try:
            with open(file_path, 'r') as f:
                for line in f:
                    # Each line is expected to have the format: Name, Gender, Count
                    name, gender, count = line.strip().split(',')
                    count = int(count)  # Convert count to integer
                    name_counts[name] += count  # Aggregate counts
        except FileNotFoundError:
            print(f"File {file_path} does not exist.")
        except PermissionError:
            print(f"Permission denied while accessing the file {file_path}.")
        except ValueError:
            print(f"Line format error in file {file_path}.")

    return name_counts  # Return name counts


def most_popular_name(directory, start_year, end_year):
    name_counts = read_baby_name_data(directory, start_year, end_year)

    if name_counts:
        # Find the most popular name
        most_popular = max(name_counts.items(), key=lambda item: item[1])
        return most_popular  # Returns a tuple (name, count)
    
    return None  # No data found


if __name__ == "__main__":
    # Example usage
    names_directory = 'names'  # Replace with your directory path
    # start_year = 1980
    # end_year = 2020
    
    most_popular = most_popular_name(names_directory, start_year, end_year)
    
    if most_popular:
        name, count = most_popular
        print(f"The most popular baby name from {start_year} to {end_year} is '{name}' with a count of {count}.")
    else:
        print(f"No data found for the years {start_year} to {end_year}.")