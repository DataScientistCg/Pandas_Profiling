import pandas as pd
from ydata_profiling import ProfileReport

# Correct path for the CSV file
df = pd.read_csv(r"C:\Users\user\OneDrive\Desktop\New folder\Pandas_Profiling\housing.csv")

# Create ProfileReport
profile = ProfileReport(df)

# Save the profile report as an HTML file
profile.to_file(output_file="housing.html")
