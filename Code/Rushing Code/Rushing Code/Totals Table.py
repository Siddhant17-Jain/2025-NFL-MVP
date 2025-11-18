import pandas as pd

# Load the team rushing data
file_path = "/Users/siddhantjain/PycharmProjects/NFL MVP/Rushing Files/Base Files/Team_Rushing.csv"
team_rushing = pd.read_csv(file_path)

# Calculate the requested statistics
team_rushing['EPA-Play'] = (team_rushing['Total EPA'] / team_rushing['Rushes']).round(2)
team_rushing['Yards per Carry'] = (team_rushing['Rush Yards'] / team_rushing['Rushes']).round(2)
team_rushing['TD %'] = (team_rushing['Rush TD'] / team_rushing['Rushes'] * 100).round(2)
team_rushing['First Down %'] = (team_rushing['First Down Rush'] / team_rushing['Rushes'] * 100).round(2)
team_rushing['Yards after Contact'] = (team_rushing['Rush Yards AC'] / team_rushing['Rushes']).round(2)
team_rushing['Tackle for Loss %'] = (team_rushing['TFL Rush'] / team_rushing['Rushes'] * 100).round(2)
team_rushing['Explosive %'] = (team_rushing['Explosive Rush'] / team_rushing['Rushes'] * 100).round(2)

# Save the updated team rushing data to a new CSV file
output_file = "/Users/siddhantjain/PycharmProjects/NFL MVP/Rushing Files/Updated_Team_Rushing.csv"
team_rushing.to_csv(output_file, index=False)

# Display a message to confirm successful calculation and saving
print(f"Updated team rushing data saved to '{output_file}'")
