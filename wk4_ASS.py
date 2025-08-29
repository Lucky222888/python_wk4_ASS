import os

def process_file_with_error_handling():
    """
    Reads a file, modifies its content, and writes to a new file,
    while handling potential file-related errors.
    """
    while True:
        input_filename = input("Please enter the name of the input file (e.g., input.txt): ")
        output_filename = input("Please enter the name for the output file (e.g., output.txt): ")

        if not input_filename or not output_filename:
            print("Both input and output filenames cannot be empty. Please try again.")
            continue

        try:
            # 1. File Read Challenge: Read the input file
            with open(input_filename, 'r', encoding='utf-8') as infile:
                original_content = infile.read()
            print(f"\nSuccessfully read content from '{input_filename}'.")
            print("--- Original Content ---")
            print(original_content)
            print("------------------------")

            # Modify the content (example modification: convert to uppercase and add a header)
            modified_content = f"--- MODIFIED BY PYTHON SCRIPT ---\n\n{original_content.upper()}\n\n--- END MODIFICATION ---"

            # 1. File Write Challenge: Write the modified content to a new file
            with open(output_filename, 'w', encoding='utf-8') as outfile:
                outfile.write(modified_content)
            print(f"\nSuccessfully wrote modified content to '{output_filename}'.")
            print("--- Modified Content (written to new file) ---")
            print(modified_content)
            print("---------------------------------------------")

            break  # Exit loop if successful

        # 2. Error Handling Lab: Handle file-related errors
        except FileNotFoundError:
            print(f"\nError: The file '{input_filename}' was not found.")
            print("Please ensure the file exists in the correct directory and try again.")
        except PermissionError:
            print(f"\nError: Permission denied to access '{input_filename}' or create '{output_filename}'.")
            print("Please check your file permissions and try again.")
        except IOError as e:
            print(f"\nAn I/O error occurred: {e}")
            print("This might be due to issues reading or writing the file.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
        finally:
            print("\nAttempt complete. If there was an error, please try again.")

# To run the program:
if __name__ == "__main__":
    print("Welcome to the File Processor!")
    process_file_with_error_handling()
    print("\nProgram finished.")

