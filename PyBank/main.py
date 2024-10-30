# -*- coding: UTF-8 -*-
import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 1
total_net = 0
first_row = ""
prev_value = 0
net_change_list = []
max_month = ""
max_value = 0
min_month = ""
min_value = 0

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_net = int(first_row[1])
    prev_value = int(first_row[1])

    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1
        current_value = int(row[1])
        total_net += current_value

        # Track the net change
        net_change = current_value - prev_value
        net_change_list.append(current_value - prev_value)

        # Calculate the greatest increase in profits (month and amount)
        if (current_value - prev_value) > max_value:
            max_month = row[0]
            max_value = current_value - prev_value

        # Calculate the greatest decrease in losses (month and amount)
        if (current_value - prev_value) < min_value:
            min_month = row[0]
            min_value = current_value - prev_value

        prev_value = current_value

# Calculate the average net change across the months
avg_net_change = sum(net_change_list) / len(net_change_list)

# Generate and print the output summary

output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${avg_net_change:.2f}\n"
    f"Greatest Increase in Profits: {max_month} (${max_value})\n"
    f"Greatest Decrease in Profits: {min_month} (${min_value})\n"
)

print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
