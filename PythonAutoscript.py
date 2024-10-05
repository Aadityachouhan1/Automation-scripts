import os

def rename_files_in_directory(directory_path, prefix):
    # Check if the directory exists
    if not os.path.exists(directory_path):
        print(f"Directory '{directory_path}' does not exist.")
        return

    # Get all files in the directory
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    # If no files are present in the directory
    if not files:
        print(f"No files found in the directory '{directory_path}'.")
        return

    # Loop through the files and rename them
    for idx, filename in enumerate(files, start=1):
        # Get file extension
        file_extension = os.path.splitext(filename)[1]
        # Create the new file name
        new_name = f"{prefix}_{idx}{file_extension}"

        # Old file path and new file path
        old_file_path = os.path.join(directory_path, filename)
        new_file_path = os.path.join(directory_path, new_name)

        # Rename the file
        os.rename(old_file_path, new_file_path)

        # Print old and new file names
        print(f"Renamed: {filename} -> {new_name}")

# Example usage
if __name__ == "__main__":
    directory = "./test_folder"  # Replace with the path to your folder
    prefix = "file"              # Prefix for the new file names
    rename_files_in_directory(directory, prefix)
