# Import csv module
import csv

# Define the file to load and the file to output
file_to_load_1 = 'data/budget_data_1.csv'
file_to_output_1 = 'output/budget_analysis_1.txt'

# Create fields to calculate based on bank revenue data
total_months_1 = 0
total_revenue_1 = 0
revenue_change_list_1 = []
greatest_increase_1 = ["", 0]
greatest_decrease_1 = ["", 0]

# Open the data file and read it into memory as a list of dictionaries with "Date" and "Revenue" keys
readcsv_1 = csv.DictReader(open(file_to_load_1))

# Skip the first row as it has the headings
start_1 = next(readcsv_1)
total_months_1 = total_months_1 + 1
total_revenue_1 = total_revenue_1 + int(start_1["Revenue"])
prev_revenue_1 = int(start_1["Revenue"])

for row in readcsv_1:

    # Add to the total months and total revenue
    total_months_1 = total_months_1 + 1
    total_revenue_1 = total_revenue_1 + int(row["Revenue"])

    # Calculate the revenue change and update the previous revenue
    revenue_change_1 = int(row["Revenue"]) - prev_revenue_1
    prev_revenue_1 = int(row["Revenue"])
    revenue_change_list_1 = revenue_change_list_1 + [revenue_change_1]

    # Determine the greatest increase in revenue
    if revenue_change_1 > greatest_increase_1[1]:
        greatest_increase_1[0] = row["Date"]
        greatest_increase_1[1] = revenue_change_1

    # Determine the greatest decrease in revenue
    if revenue_change_1 < greatest_decrease_1[1]:
        greatest_decrease_1[0] = row["Date"]
        greatest_decrease_1[1] = revenue_change_1

# Calculate the average revenue change
revenue_avg_1 = sum(revenue_change_list_1)/len(revenue_change_list_1)

# Generate output summary
output_1 = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months_1}\n"
    f"Total Revenue: ${total_revenue_1}\n"
    f"Average Revenue Change: ${revenue_avg_1}\n"
    f"Greatest Increase in Revenue: {greatest_increase_1[0]} (${greatest_increase_1[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease_1[0]} (${greatest_decrease_1[1]})\n")

# Print the output (to terminal)
print(output_1)

# Export the results to text file
with open(file_to_output_1, "w") as txt_file:
    txt_file.write(output_1)

# REPEAT ALL STEPS WITH BUDGET_DATA_2

# Define the file to load and the file to output
file_to_load_2 = 'data/budget_data_2.csv'
file_to_output_2 = 'output/budget_analysis_2.txt'

# Create fields to calculate based on bank revenue data
total_months_2 = 0
total_revenue_2 = 0
revenue_change_list_2 = []
greatest_increase_2 = ["", 0]
greatest_decrease_2 = ["", 0]

# Open the data file and read it into memory as a list of dictionaries with "Date" and "Revenue" keys
readcsv_2 = csv.DictReader(open(file_to_load_2))

# Skip the first row as it has the headings
start_2 = next(readcsv_2)
total_months_2 = total_months_2 + 1
total_revenue_2 = total_revenue_2 + int(start_2["Revenue"])
prev_revenue_2 = int(start_2["Revenue"])

for row in readcsv_2:

    # Add to the total months and total revenue
    total_months_2 = total_months_2 + 1
    total_revenue_2 = total_revenue_2 + int(row["Revenue"])

    # Calculate the revenue change and update the previous revenue
    revenue_change_2 = int(row["Revenue"]) - prev_revenue_2
    prev_revenue_2 = int(row["Revenue"])
    revenue_change_list_2 = revenue_change_list_2 + [revenue_change_2]

    # Determine the greatest increase in revenue
    if revenue_change_2 > greatest_increase_2[1]:
        greatest_increase_2[0] = row["Date"]
        greatest_increase_2[1] = revenue_change_2

    # Determine the greatest decrease in revenue
    if revenue_change_2 < greatest_decrease_2[1]:
        greatest_decrease_2[0] = row["Date"]
        greatest_decrease_2[1] = revenue_change_2

# Calculate the average revenue change
revenue_avg_2 = sum(revenue_change_list_2)/len(revenue_change_list_2)

# Generate output summary
output_2 = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months_2}\n"
    f"Total Revenue: ${total_revenue_2}\n"
    f"Average Revenue Change: ${revenue_avg_2}\n"
    f"Greatest Increase in Revenue: {greatest_increase_2[0]} (${greatest_increase_2[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease_2[0]} (${greatest_decrease_2[1]})\n")

# Print the output (to terminal)
print(output_2)

# Export the results to text file
with open(file_to_output_2, "w") as txt_file:
    txt_file.write(output_2)