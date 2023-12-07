# Specify the path to the README.md file
file_path = 'README.md'

# Read the contents of the file
with open(file_path, 'r') as file:
    content = file.readlines()

# Add a newline character at the end of each line
content = [line.rstrip() + '\n' for line in content]

# Write the updated contents back to the file
with open(file_path, 'w') as file:
    file.writelines(content)