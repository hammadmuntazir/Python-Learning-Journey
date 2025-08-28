import os

def list_directory_contents(directory):
  """Prints the names of all files and directories within the specified directory."""
  for item in os.listdir(directory):
    print(item)

# Get the directory path from the user
directory_path = input("Enter the directory path: ")

# Print the contents of the directory
list_directory_contents(directory_path)