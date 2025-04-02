# app/io/output.py

def print_text_to_console(text):
    """
    Prints text to the console.
    Args:
        text (str): The text to be printed.
    """
    print(text)

def write_text_to_file(filepath, text):
    """
    Writes text to a file using built-in Python capabilities.
    Args:
        filepath (str): Path to the file.
        text (str): The text to be written.
    """
    try:
        with open(filepath, "w") as file:
            file.write(text)
    except Exception as e:
        print(f"Error writing to file: {e}")
