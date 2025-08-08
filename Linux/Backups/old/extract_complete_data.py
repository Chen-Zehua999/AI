import pandas as pd
import re

# Read the Excel file
df = pd.read_excel('Linux Marking Scheme.xlsx')

print("Extracting all aspects with commands and expected outputs...")

aspects = []

for i in range(len(df)):
    # Get aspect description from column 4
    aspect_desc = df.iloc[i, 4]  # Column 4: Aspect Description
    commands = df.iloc[i, 6]     # Column 6: Commands
    expected_output = df.iloc[i, 7]  # Column 7: Expected Output
    
    # Skip if aspect description is empty or NaN
    if pd.isna(aspect_desc) or not isinstance(aspect_desc, str):
        continue
    
    # Skip if commands is empty or NaN
    if pd.isna(commands) or not isinstance(commands, str):
        continue
    
    # Clean the commands - remove the grading wrapper and "Executed command on..." lines
    clean_commands = commands
    
    # Remove lines starting with "./grading -v -t"
    clean_commands = re.sub(r'./grading -v -t [^\n]*\n?', '', clean_commands)
    
    # Remove lines starting with "Executed command on"
    clean_commands = re.sub(r'Executed command on [^\n]*=>\n?', '', clean_commands)
    
    # Clean up extra whitespace and newlines
    clean_commands = re.sub(r'\n\s*\n', '\n', clean_commands)
    clean_commands = clean_commands.strip()
    
    # Skip if no commands remain after cleaning
    if not clean_commands:
        continue
    
    # Format expected output
    clean_expected = str(expected_output) if pd.notna(expected_output) else ""
    
    aspects.append({
        'aspect': aspect_desc,
        'commands': clean_commands,
        'expected_output': clean_expected
    })

print(f"Found {len(aspects)} aspects with commands and expected outputs:")
print("="*80)

for i, aspect in enumerate(aspects, 1):
    print(f"\n{i}. ASPECT: {aspect['aspect']}")
    print(f"COMMANDS:\n{aspect['commands'][:200]}...")
    print(f"EXPECTED OUTPUT:\n{aspect['expected_output'][:200]}...")
    print("-"*60)

# Save to a text file for reference
with open('extracted_aspects.txt', 'w', encoding='utf-8') as f:
    for i, aspect in enumerate(aspects, 1):
        f.write(f"{i}. ASPECT: {aspect['aspect']}\n")
        f.write(f"COMMANDS:\n{aspect['commands']}\n\n")
        f.write(f"EXPECTED OUTPUT:\n{aspect['expected_output']}\n")
        f.write("="*80 + "\n\n")

print(f"\nData saved to 'extracted_aspects.txt'")
print(f"Total aspects found: {len(aspects)}") 