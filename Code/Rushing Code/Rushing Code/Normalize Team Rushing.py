import pandas as pd

# Load the combined data
file_path = "/Users/siddhantjain/PycharmProjects/NFL MVP/Rushing Files/Updated_Team_Rushing.csv"
data = pd.read_csv(file_path)

# Convert percentage strings to numeric values if they exist
for column in data.columns[1:]:  # Skip the "Team" column
    if data[column].dtype == 'object' and data[column].str.contains('%').any():
        data[column] = data[column].str.replace('%', '').astype(float)

# Define the columns where lower is better and where higher is better
higher_is_better = ["Rushes","EPA-Play","Yards per Carry","TD %","First Down %","Yards after Contact","Explosive %"]
lower_is_better = ["Tackle for Loss %"]

# Normalize the data
for column in data.columns[1:]:  # Skip the "Team" column
    league_avg = data[column].mean()  # Calculate league average
    if column in lower_is_better:
        # If values are negative, shift the column to be all positive
        if data[column].min() < 0:
            shift = abs(data[column].min()) + 1  # Add a constant to shift all values to > 0
            data[column] += shift
            league_avg += shift
        # Normalize: lower values are better
        data[column] = (league_avg / data[column]) * 100
    elif column in higher_is_better:
        # If values are negative, shift the column to be all positive
        if data[column].min() < 0:
            shift = abs(data[column].min()) + 1  # Add a constant to shift all values to > 0
            data[column] += shift
            league_avg += shift
        # Normalize: higher values are better
        data[column] = (data[column] / league_avg) * 100

# Ensure all values are greater than zero (as a safety measure)
data.iloc[:, 1:] = data.iloc[:, 1:].clip(lower=0)

# Round all numeric columns to 2 decimal places
data.iloc[:, 1:] = data.iloc[:, 1:].round(2)

# Save the normalized data to a new CSV file
output_file_path = "/Users/siddhantjain/PycharmProjects/NFL MVP/Rushing Files/Normalized_Team_Rushing.csv"
data.to_csv(output_file_path, index=False)

# Display a message to confirm successful saving
print(f"Normalized data saved to '{output_file_path}'")
