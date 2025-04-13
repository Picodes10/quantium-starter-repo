import pandas as pd
import glob

# Step 1: Load all CSV files from the data folder
file_paths = glob.glob('data/*.csv')  # Adjust path as needed
df_list = []

for path in file_paths:
    df = pd.read_csv(path)

    # Step 2: Filter for only 'Pink Morsels'
    df = df[df['product'] == 'Pink Morsels']

    # Step 3: Calculate 'sales'
    df['sales'] = df['quantity'] * df['price']

    # Step 4: Keep only required columns
    df_filtered = df[['sales', 'date', 'region']]

    df_list.append(df_filtered)

# Step 5: Combine all dataframes
final_df = pd.concat(df_list, ignore_index=True)

# Step 6: Save to output CSV
final_df.to_csv('formatted_sales.csv', index=False)

print("✅ Output saved to 'formatted_sales.csv'")
