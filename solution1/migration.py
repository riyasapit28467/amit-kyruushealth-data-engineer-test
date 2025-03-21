import psycopg2
import os

def get_connection():
    """Create and return a connection to the PostgreSQL database."""
    return psycopg2.connect(
        dbname='popular_names',
        user='postgres',
        password='postgres',
        host='localhost',  # change if needed
        port='5432'        # change if needed
    )

def create_table():
    """Create the users table if it does not exist."""
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                gender CHAR(1),
                occurrence INT,
                year INT
            );
            '''
            cursor.execute(create_table_query)
            connection.commit()
            print("Table 'users' created successfully.")
    except psycopg2.Error as error:
        print(f"Error while creating table: {error}")

def insert_user(name, gender, occurrence, year):
    """Insert a user into the users table."""
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            insert_query = '''
            INSERT INTO users (name, gender, occurrence, year)
            VALUES (%s, %s, %s, %s);
            '''
            cursor.execute(insert_query, (name, gender, occurrence, year))
            connection.commit()
            print(f"Inserted user: {name}, {gender}, {occurrence}, {year}")
    except psycopg2.Error as error:
        print(f"Error while inserting data into PostgreSQL: {error}")

def process_files_and_insert_users(directory):
    """Process text files in the given directory and insert user records into the database."""
    if not os.path.isdir(directory):
        print(f"Directory {directory} does not exist.")
        return

    for filename in os.listdir(directory):
        if filename.startswith("yob") and filename.endswith(".txt"):
            # Extract year from the filename. Assuming format 'yobYYYY.txt'
            year = filename[3:7]  # Get the substring 'YYYY' from the filename
            with open(os.path.join(directory, filename), 'r') as file:
                lines = [line.strip() for line in file]  # Read all lines into a list

            # Process all entries in the file
            for line in lines:
                try:
                    name, gender, occurrence = line.split(',')
                    insert_user(name, gender, int(occurrence), int(year))
                except ValueError:
                    print(f"Error processing line: '{line}' in file: '{filename}'. Make sure it is in the format 'name,gender,occurrence'.")

if __name__ == "__main__":
    create_table()  # Create the table at the start
    process_files_and_insert_users('names')