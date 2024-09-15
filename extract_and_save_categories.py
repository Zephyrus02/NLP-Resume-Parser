import pandas as pd
import json

# Load the dataset (adjust the path to your CSV file)
csv_path = 'UpdatedResumeDataSet.csv'  # Replace with your actual CSV path
df = pd.read_csv(csv_path)

# Extract job categories
job_categories = list(df['Category'].astype('category').cat.categories)

# Save categories to a JSON file
categories_path = 'job_categories.json'  # Save categories in the same folder as the CSV
with open(categories_path, 'w') as f:
    json.dump(job_categories, f)

print(f"Job categories saved to {categories_path}")
