import pandas as pd

# File paths
folder_path = "/Users/siddhantjain/PycharmProjects/NFL MVP/Rushing Files/Base Files/"
advanced_rushing_file = folder_path + "Advanced Rushing.csv"
nfl_rushing_file = folder_path + "NFL Rushing.csv"

# Load the data
advanced_rushing = pd.read_csv(advanced_rushing_file)
nfl_rushing = pd.read_csv(nfl_rushing_file)

# Clean the "Name" column in the Advanced Rushing file to remove rank numbers
advanced_rushing['Name'] = advanced_rushing['Name'].str.replace(r"^\d+\.\s*", "", regex=True)

# Combine the files based on the "Name" column
combined_rushing = pd.merge(advanced_rushing, nfl_rushing, on="Name", how="inner")

# Save the combined data to a new CSV file
output_file = folder_path + "Combined_Rushing.csv"
combined_rushing.to_csv(output_file, index=False)

# Display a message to confirm successful combination
print(f"Combined data saved to '{output_file}'")
