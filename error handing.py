def read_file(filename):
    """Reads the content of a file and returns it."""
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, content):
    """Writes content to a file."""
    with open(filename, 'w') as file:
        file.write(content)

def modify_content(content):
    """Modifies the content (example: converts to uppercase)."""
    return content.upper()  # You can change this to any modification you need.

def main():
    # Ask the user for a filename
    input_filename = input("Please enter the filename to read: ")
    
    try:
        # Attempt to read the file
        content = read_file(input_filename)
        
        # Modify the content
        modified_content = modify_content(content)
        
        # Define the output filename
        output_filename = "modified_" + input_filename
        
        # Write the modified content to a new file
        write_file(output_filename, modified_content)
        
        print(f"Modified content has been written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' could not be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()