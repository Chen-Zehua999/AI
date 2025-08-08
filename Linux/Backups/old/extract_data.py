import pandas as pd

# Read the Excel file
df = pd.read_excel('Linux Marking Scheme.xlsx')

print("Excel file structure:")
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")

print("\nFirst few rows:")
for i in range(min(10, len(df))):
    print(f"\nRow {i}:")
    for j, col in enumerate(df.columns):
        value = df.iloc[i, j]
        if pd.notna(value):
            print(f"  Column {j} ({col}): {str(value)[:200]}...")

print("\nLooking for commands and expected outputs...")
# Look for rows that might contain commands or expected outputs
for i in range(len(df)):
    for j, col in enumerate(df.columns):
        value = df.iloc[i, j]
        if pd.notna(value) and isinstance(value, str):
            if any(keyword in value.lower() for keyword in ['command', 'grading', 'ldap', 'ssh', 'sudo']):
                print(f"\nRow {i}, Column {j}: {str(value)[:300]}...") 