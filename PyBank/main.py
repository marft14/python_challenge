# Define file paths
file_path = 'Resources/budget_data.csv' 
output_file_path = 'analysis/financial_analysis.txt'

# Initialize variables to store data
dates = []
profits_losses = []
changes = []

# Read the CSV file 
with open(file_path, 'r') as f:
    next(f)  # Skip the header
    previous_profit_loss = None

    for line in f:
        date, profit_loss = line.strip().split(',')
        profit_loss = int(profit_loss)
        
        dates.append(date)
        profits_losses.append(profit_loss)
        
        # Calculate the change in profit/losses if not the first record
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)
        previous_profit_loss = profit_loss

# Calculate the total months
total_months = len(dates)

# Calculate the net total profit/losses
net_total = sum(profits_losses)

# Calculate the average change (skip the first month as there's no prior month to compare)
average_change = sum(changes) / len(changes) if changes else 0

# Find the greatest increase and decrease in profits
greatest_increase = max(changes) if changes else 0
greatest_increase_index = changes.index(greatest_increase) if changes else -1
greatest_decrease = min(changes) if changes else 0
greatest_decrease_index = changes.index(greatest_decrease) if changes else -1

# Prepare output
output = [
    "Financial Analysis",
    "----------------------------",
    f"Total Months: {total_months}",
    f"Net Total Profit/Losses: ${net_total}",
    f"Average Change in Profit/Losses: ${average_change:.2f}",
    f"Greatest Increase in Profits: {dates[greatest_increase_index + 1]} (${greatest_increase})" if greatest_increase_index != -1 else "No data for increase",
    f"Greatest Decrease in Profits: {dates[greatest_decrease_index + 1]} (${greatest_decrease})" if greatest_decrease_index != -1 else "No data for decrease"
]

# Write results to output file
with open(output_file_path, 'w') as f:
    for line in output:
        f.write(line + '\n')

# Display the final output
print("\n".join(output))