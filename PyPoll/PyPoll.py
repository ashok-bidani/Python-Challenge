# Import the csv module
import csv

# Define the file to load and the file to output
file_to_load_1 = "data/election_data_1.csv"
file_to_output_1 = "output/election_analysis_1.txt"

# Create a total vote counter
total_votes_1 = 0

# Create candidate options and candidate vote counters
candidate_options_1 = []
candidate_votes_1 = {}

# Create winning candidate and winning vote count fields
winning_candidate_1 = ""
winning_count_1 = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load_1) as election_data_1:
    readcsv_1 = csv.DictReader(election_data_1)

    # For each row...
    for row in readcsv_1:

        # Add to the total vote count
        total_votes_1 = total_votes_1 + 1

        # Extract the candidate name from each row
        candidate_name_1 = row["Candidate"]

        # If the candidate does not match any existing candidate...
        # (In a way, the loop is "discovering" candidates as it goes)
        if candidate_name_1 not in candidate_options_1:

            # Add it to the list of candidates in the running
            candidate_options_1.append(candidate_name_1)

            # And begin tracking that candidate's voter count
            candidate_votes_1[candidate_name_1] = 0

        # Then add a vote to that candidate's count
        candidate_votes_1[candidate_name_1] = candidate_votes_1[candidate_name_1] + 1

# Print the results and export the data to our text file
with open(file_to_output_1, "w") as txt_file_1:

    # Print the final vote count (to terminal)
    election_results_1 = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes_1}\n"
        f"-------------------------\n")
    print(election_results_1, end="")

    # Save the final vote count to the text file
    txt_file_1.write(election_results_1)

    # Determine the winner by looping through the counts
    for candidate_1 in candidate_votes_1:

        # Retrieve vote count and percentage
        votes_1 = candidate_votes_1.get(candidate_1)
        vote_percentage_1 = float(votes_1)/float(total_votes_1) * 100

        # Determine winning vote count and candidate
        if (votes_1 > winning_count_1):
            winning_count_1 = votes_1
            winning_candidate_1 = candidate_1

        # Print each candidate's voter count and percentage (to terminal)
        voter_output_1 = f"{candidate_1}: {vote_percentage_1:.3f}% ({votes_1})\n"
        print(voter_output_1, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file_1.write(voter_output_1)

    # Print the winning candidate (to terminal)
    winning_candidate_summary_1 = (
        f"-------------------------\n"
        f"Winner: {winning_candidate_1}\n"
        f"-------------------------\n")
    print(winning_candidate_summary_1)

    # Save the winning candidate's name to the text file
    txt_file_1.write(winning_candidate_summary_1)

# REPEAT ALL STEPS WITH EMPLOYEE_DATA2

# Define the file to load and the file to output
file_to_load_2 = "data/election_data_2.csv"
file_to_output_2 = "output/election_analysis_2.txt"

# Create a total vote counter
total_votes_2 = 0

# Create candidate options and candidate vote counters
candidate_options_2 = []
candidate_votes_2 = {}

# Create winning candidate and winning vote count fields
winning_candidate_2 = ""
winning_count_2 = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load_2) as election_data_2:
    readcsv_2 = csv.DictReader(election_data_2)

    # For each row...
    for row in readcsv_2:

        # Add to the total vote count
        total_votes_2 = total_votes_2 + 1

        # Extract the candidate name from each row
        candidate_name_2 = row["Candidate"]

        # If the candidate does not match any existing candidate...
        # (In a way, the loop is "discovering" candidates as it goes)
        if candidate_name_2 not in candidate_options_2:

            # Add it to the list of candidates in the running
            candidate_options_2.append(candidate_name_2)

            # And begin tracking that candidate's voter count
            candidate_votes_2[candidate_name_2] = 0

        # Then add a vote to that candidate's count
        candidate_votes_2[candidate_name_2] = candidate_votes_2[candidate_name_2] + 1

# Print the results and export the data to our text file
with open(file_to_output_2, "w") as txt_file_2:

    # Print the final vote count (to terminal)
    election_results_2 = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes_2}\n"
        f"-------------------------\n")
    print(election_results_2, end="")

    # Save the final vote count to the text file
    txt_file_2.write(election_results_2)

    # Determine the winner by looping through the counts
    for candidate_2 in candidate_votes_2:

        # Retrieve vote count and percentage
        votes_2 = candidate_votes_2.get(candidate_2)
        vote_percentage_2 = float(votes_2)/float(total_votes_2) * 100

        # Determine winning vote count and candidate
        if (votes_2 > winning_count_2):
            winning_count_2 = votes_2
            winning_candidate_2 = candidate_2

        # Print each candidate's voter count and percentage (to terminal)
        voter_output_2 = f"{candidate_2}: {vote_percentage_2:.3f}% ({votes_2})\n"
        print(voter_output_2, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file_2.write(voter_output_2)

    # Print the winning candidate (to terminal)
    winning_candidate_summary_2 = (
        f"-------------------------\n"
        f"Winner: {winning_candidate_2}\n"
        f"-------------------------\n")
    print(winning_candidate_summary_2)

    # Save the winning candidate's name to the text file
    txt_file_2.write(winning_candidate_summary_2)