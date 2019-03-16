# Import necessary modules
import csv
import datetime

# Define the file to load and the file to output
file_to_load_1 = "data/employee_data1.csv"
file_to_output_1 = "output/employee_data_reformatted1.csv"

# Include a dictionary of states with abbreviations
us_state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

# Create fields for re-formatted contents
emp_ids_1 = []
emp_first_names_1 = []
emp_last_names_1 = []
emp_dobs_1 = []
emp_ssns_1 = []
emp_states_1 = []

# Read the csv and convert it into a list of dictionaries
with open(file_to_load_1) as emp_data_1:
    readcsv_1 = csv.DictReader(emp_data_1)

    # Loop through each row, select each field and store it in a new list
    for row in readcsv_1:

        # Select emp_ids and store it into a list
        emp_ids_1 = emp_ids_1 + [row["Emp ID"]]

        # Select names, split them, and store them in a temporary variable
        split_name_1 = row["Name"].split(" ")

        # Then save first and last name in separate lists
        emp_first_names_1 = emp_first_names_1 + [split_name_1[0]]
        emp_last_names_1 = emp_last_names_1 + [split_name_1[1]]

        # Select DOB and reformat it
        reformatted_dob_1 = datetime.datetime.strptime(row["DOB"], "%Y-%m-%d")
        reformatted_dob_1 = reformatted_dob_1.strftime("%m/%d/%Y")

        # Then store it into a list
        emp_dobs_1 = emp_dobs_1 + [reformatted_dob_1]

        # Select SSN and reformat it
        split_ssn_1 = list(row["SSN"])
        split_ssn_1[0:3] = ("*", "*", "*")
        split_ssn_1[4:6] = ("*", "*")
        joined_ssn_1 = "".join(split_ssn_1)

        # Then store it into a list
        emp_ssns_1 = emp_ssns_1 + [joined_ssn_1]

        # Select the states and use the dictionary to find the replacement
        state_abbrev_1 = us_state_abbrev[row["State"]]

        # Then store the abbreviation into a list
        emp_states_1 = emp_states_1 + [state_abbrev_1]

# Zip all of the new lists together
emp_db_1 = zip(emp_ids_1, emp_first_names_1, emp_last_names_1,
            emp_dobs_1, emp_ssns_1, emp_states_1)

# Write all of the election data to csv
with open(file_to_output_1, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Emp ID", "First Name", "Last Name",
                     "DOB", "SSN", "State"])
    writer.writerows(emp_db_1)

# REPEAT ALL STEPS WITH EMPLOYEE_DATA2

# Define the file to load and the file to output
file_to_load_2 = "data/employee_data2.csv"
file_to_output_2 = "output/employee_data_reformatted2.csv"

# Create fields for re-formatted contents
emp_ids_2 = []
emp_first_names_2 = []
emp_last_names_2 = []
emp_dobs_2 = []
emp_ssns_2 = []
emp_states_2 = []

# Read the csv and convert it into a list of dictionaries
with open(file_to_load_2) as emp_data_2:
    readcsv_2 = csv.DictReader(emp_data_2)

    # Loop through each row, select each field and store it in a new list
    for row in readcsv_2:

        # Select emp_ids and store it into a list
        emp_ids_2 = emp_ids_2 + [row["Emp ID"]]

        # Select names, split them, and store them in a temporary variable
        split_name_2 = row["Name"].split(" ")

        # Then save first and last name in separate lists
        emp_first_names_2 = emp_first_names_2 + [split_name_2[0]]
        emp_last_names_2 = emp_last_names_2 + [split_name_2[1]]

        # Select DOB and reformat it
        reformatted_dob_2 = datetime.datetime.strptime(row["DOB"], "%Y-%m-%d")
        reformatted_dob_2 = reformatted_dob_2.strftime("%m/%d/%Y")

        # Then store it into a list
        emp_dobs_2 = emp_dobs_2 + [reformatted_dob_2]

        # Select SSN and reformat it
        split_ssn_2 = list(row["SSN"])
        split_ssn_2[0:3] = ("*", "*", "*")
        split_ssn_2[4:6] = ("*", "*")
        joined_ssn_2 = "".join(split_ssn_2)

        # Then store it into a list
        emp_ssns_2 = emp_ssns_2 + [joined_ssn_2]

        # Select the states and use the dictionary to find the replacement
        state_abbrev_2 = us_state_abbrev[row["State"]]

        # Then store the abbreviation into a list
        emp_states_2 = emp_states_2 + [state_abbrev_2]

# Zip all of the new lists together
emp_db_2 = zip(emp_ids_2, emp_first_names_2, emp_last_names_2,
            emp_dobs_2, emp_ssns_2, emp_states_2)

# Write all of the election data to csv
with open(file_to_output_2, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Emp ID", "First Name", "Last Name",
                     "DOB", "SSN", "State"])
    writer.writerows(emp_db_2)