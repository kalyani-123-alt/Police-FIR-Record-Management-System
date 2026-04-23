import csv
import os
import re
from datetime import datetime

# File name where FIR records are stored
filename = 'fir_records.csv'

# Predefined username and password (for simplicity, stored in the script)
USERNAME = "admin"
PASSWORD = "admin123"

# Function to initialize the CSV file with headers if it doesn't exist
def initialize_csv():
    if not os.path.exists(filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                "Case Number", "Date of Report", "Complainant Name", "Gender", "Age", "Weight", "Height",
                "Hair Color", "Eye Color", "Case Description", "Status", "Police Station",
                "Emergency Mobile Number", "Court", "Crime Happened Area", "Last Updated"
            ])

# Function to validate phone number (basic format)
def is_valid_phone(phone):
    return bool(re.match(r'^[0-9]{10}$', phone))

# Function to authenticate user
def login():
    print("\nPlease log in to access the FIR system.")
    attempts = 3  # Max login attempts
    while attempts > 0:
        username = input("Username: ")
        password = input("Password: ")

        if username == USERNAME and password == PASSWORD:
            print("\nLogin successful!")
            return True
        else:
            attempts -= 1
            print(f"Invalid credentials! You have {attempts} attempts left.")
            if attempts == 0:
                print("Too many failed attempts. Exiting...")
                return False

# Function to add a new FIR record
def add_fir():
    case_number = input("Enter Case Number: ")
    date_of_report = input("Enter Date of Report (DD-MM-YYYY): ")
    complainant_name = input("Enter Complainant Name: ")
    gender = input("Enter Gender (Male/Female/Other): ")
    age = input("Enter Age: ")
    weight = input("Enter Weight (kg): ")
    height = input("Enter Height (cm): ")
    hair_color = input("Enter Hair Color: ")
    eye_color = input("Enter Eye Color: ")
    case_description = input("Enter Case Description: ")
    status = input("Enter Status (open/closed): ")
    police_station = input("Enter Police Station: ")
    emergency_mobile_number = input("Enter Emergency Mobile Number: ")
    while not is_valid_phone(emergency_mobile_number):
        print("Invalid phone number. It should be a 10-digit number.")
        emergency_mobile_number = input("Enter Emergency Mobile Number: ")
    court = input("Enter Court details: ")
    crime_happened_area = input("Enter Crime Happened Area: ")

    # Get current timestamp for the 'Last Updated' field
    last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Write data to CSV
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            case_number, date_of_report, complainant_name, gender, age, weight, height,
            hair_color, eye_color, case_description, status, police_station,
            emergency_mobile_number, court, crime_happened_area, last_updated
        ])

    print("FIR added successfully!")

# Function to view all FIR records with better formatting
def view_firs():
    print("\nFIR Records:")
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Skip the header row
        print(f"{' | '.join(headers)}")
        for row in reader:
            print(f"{' | '.join(row)}")

# Function to search FIR by Case Number (case insensitive)
def search_fir():
    case_number = input("Enter Case Number to search: ").lower()
    found = False
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Skip header row
        for row in reader:
            if row[0].lower() == case_number:
                print("\nFIR Found:")
                print(f"{' | '.join(headers)}")
                print(f"{' | '.join(row)}")
                found = True
                break
    if not found:
        print("FIR not found!")

# Function to update an FIR record
def update_fir():
    case_number = input("Enter Case Number to update: ").lower()
    rows = []
    updated = False
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        headers = rows[0]  # The first row is the header
        writer.writerow(headers)  # Write headers back
        for row in rows[1:]:
            if row[0].lower() == case_number:
                print("FIR Found. You can update the following fields:")
                # Asking for new values and updating the fields
                date_of_report = input("Enter Date of Report (DD-MM-YYYY): ")
                complainant_name = input("Enter Complainant Name: ")
                gender = input("Enter Gender (Male/Female/Other): ")
                age = input("Enter Age: ")
                weight = input("Enter Weight (kg): ")
                height = input("Enter Height (cm): ")
                hair_color = input("Enter Hair Color: ")
                eye_color = input("Enter Eye Color: ")
                case_description = input("Enter Case Description: ")
                status = input("Enter Status (open/closed): ")
                police_station = input("Enter Police Station: ")
                emergency_mobile_number = input("Enter Emergency Mobile Number: ")
                court = input("Enter Court details: ")
                crime_happened_area = input("Enter Crime Happened Area: ")
                last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                writer.writerow([  # Update the FIR
                    row[0], date_of_report, complainant_name, gender, age, weight, height,
                    hair_color, eye_color, case_description, status, police_station,
                    emergency_mobile_number, court, crime_happened_area, last_updated
                ])
                updated = True
            else:
                writer.writerow(row)  # Keep the old record as is

    if updated:
        print(f"FIR with Case Number {case_number} updated successfully!")
    else:
        print("FIR not found!")

# Main Menu Function
def menu():
    while True:
        print("\nPolice FIR Record Management System")
        print("1. Add FIR")
        print("2. View All FIRs")
        print("3. Search FIR")
        print("4. Update FIR")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_fir()
        elif choice == '2':
            view_firs()
        elif choice == '3':
            search_fir()
        elif choice == '4':
            update_fir()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

# Initialize the CSV file (if not exists)
initialize_csv()

# Ask for login before proceeding to the main menu
if login():
    # Start the menu if login is successful
    menu()
else:
    print("Access Denied. Program Exiting...")
