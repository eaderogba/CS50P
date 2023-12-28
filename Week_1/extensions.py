# Program prompts user for the name of a file
def main():
    file_name = input("Enter the name of a file: ")
    media_type = get_file_extension(file_name)
    # Program outputs file's media type
    print(media_type)

# Function to determine the media type of a file based on its extension
def get_file_extension(filename):
    # Dictionary mapping file extensions to media types
    media_types = {
        "gif": "image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip",
    }

    # Remove spaces from the filename and extract the file extension
    parts = filename.replace(" ", "").rsplit(".", 1)

    # Check if a valid file extension exists and return the corresponding media type
    if len(parts) == 2:
        extension = parts[1].lower()

        if extension in media_types:
            return media_types[extension]
    # Default media type if the extension is not recognized
    return "application/octet-stream"


main()
