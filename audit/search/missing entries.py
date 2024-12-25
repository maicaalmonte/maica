import pandas as pd

# Load the main dataset containing invoice numbers
file_path1 = r'C:\Users\jamai\OneDrive\Desktop\FindingInvoices.xlsx'
df6 = pd.read_excel(file_path1, sheet_name='TOTAL')
invoice_numbers_6char = df6['NUM']

# Extract prefixes and numbers from invoice numbers
prefixes_6char = invoice_numbers_6char.str[:2]
numbers_6char = invoice_numbers_6char.str[2:]

# Count occurrences of each prefix
counts_6char = prefixes_6char.value_counts()

# Define the prefix and starting number for the range
prefix = "DR"
start_num = 8018

# Generate possible invoice numbers in the specified range
possible_numbers_6char = [f"{prefix}{n:04}" for n in range(start_num, start_num + 1000)]

# Identify missing invoice numbers
missing_numbers_6char = set(possible_numbers_6char) - set(invoice_numbers_6char)

# Save missing numbers to a new file for analysis
output_file_path = r'C:\Users\jamai\OneDrive\Desktop\mia_numbers.xlsx'
pd.DataFrame(list(missing_numbers_6char), columns=['Missing NUM']).to_excel(output_file_path, index=False)

print(f"Missing invoice numbers saved to: {output_file_path}")
