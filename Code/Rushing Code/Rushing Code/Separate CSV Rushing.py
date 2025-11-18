import os
import pandas as pd

# Step 1: Load the dataset
file_path = '/Users/siddhantjain/PycharmProjects/NFL MVP/Rushing Files/Normalized_Team_Rushing.csv'
df = pd.read_csv(file_path)

# Step 2: Define the columns to rank
metrics = [
    "EPA-Play","Yards per Carry","TD %","First Down %",
    "Yards after Contact","Tackle for Loss %","Explosive %"
]

# Step 3: Create the output directory if it doesn't exist
output_dir = '/Users/siddhantjain/PycharmProjects/NFL MVP/Rushing Files/Separate CSV'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Step 4: Rank the metrics
for column in metrics:
    # Ensure that the column exists in the DataFrame
    if column in df.columns:
        # Rank the column in descending order (higher is better)
        df[column + "_Rank"] = df[column].rank(ascending=False, method='min')

# Step 5: Create new CSV files for each metric with rankings
for column in metrics:
    if column in df.columns:
        # Create a new DataFrame with the 'Team' and the ranked metric
        ranked_df = df[['Team', column, column + "_Rank"]]

        # Create the output file path within the 'Separate CSV' folder
        output_file = os.path.join(output_dir, f"{column.replace(' ', '_')}_Ranked.csv")

        # Save the ranked DataFrame to a new CSV file
        ranked_df.to_csv(output_file, index=False)

print("CSV files with ranked metrics have been created in the 'Separate CSV' folder.")
