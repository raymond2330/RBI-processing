import pandas as pd

# Load the Excel file
excel_path = "RBI 2024 sample.xlsx"  # Replace with the path to your Excel file
xls = pd.ExcelFile(excel_path)

# Load the first sheet
df = xls.parse(xls.sheet_names[0])

# Step 1: Remove non-data rows and fully empty rows
df_cleaned = df.dropna(how='all')  # Drop rows that are completely empty
df_cleaned = df_cleaned[df_cleaned['LAST'] != 'HOUSEHOLD MEMBER/S']  # Remove internal headers

# Step 2: Create a new column indicating if the person is the household head
df_cleaned['Is Household Head'] = df_cleaned['RELATIONSHIP TO HOUSEHOLD HEAD'].apply(
    lambda x: 'Yes' if isinstance(x, str) and x.strip().lower() == 'household head' else 'No'
)

# Step 3: Normalize date format
df_cleaned['DATE OF BIRTH'] = pd.to_datetime(df_cleaned['DATE OF BIRTH'], errors='coerce').dt.date

# Step 4: Save to CSV
csv_path = "RBI_2024_cleaned.csv"
df_cleaned.to_csv(csv_path, index=False)

print(f"Cleaned CSV saved to: {csv_path}")
