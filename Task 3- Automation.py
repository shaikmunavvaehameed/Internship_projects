import re

# Input and output file names
input_file = "sample_text.txt"
output_file = "extracted_emails.txt"

# Read the contents of the input file
with open(input_file, "r") as file:
    text = file.read()

# Use regex to find all email addresses
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattern, text)

# Remove duplicates (if any)
unique_emails = list(set(emails))

# Write emails to the output file
with open(output_file, "w") as file:
    for email in unique_emails:
        file.write(email + "\n")

print(f"Extracted {len(unique_emails)} email(s) and saved to '{output_file}'.")
