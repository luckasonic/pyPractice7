def read_text_from_console():
    """
    Reads text from the console.
    Returns:
        str: The text entered by the user.
    """
    return input("Enter text: ")

def read_text_from_file(filepath):
    """
    Reads text from a file using built-in Python capabilities.
    Args:
        filepath (str): Path to the file.
    Returns:
        str: The content of the file.
    """
    try:
        with open(filepath, "r") as file:
            return file.read()
    except FileNotFoundError:
        return f"File not found: {filepath}"

def read_text_from_file_with_pandas(filepath):
    """
    Reads text from a file using the pandas library.
    Args:
        filepath (str): Path to the file.
    Returns:
        str: The content of the file as a single string.
    """
    import pandas as pd
    try:
        df = pd.read_csv(filepath)
        return df.to_string()
    except FileNotFoundError:
        return f"File not found: {filepath}"
    except pd.errors.EmptyDataError:
        return f"File is empty: {filepath}"