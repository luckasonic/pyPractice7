# main.py

from app.io.input import read_text_from_console, read_text_from_file, read_text_from_file_with_pandas
from app.io.output import print_text_to_console, write_text_to_file

def main():
    """
    Main function to start the application.
    Calls functions for input and output of text.
    """
    print_text_to_console("Starting the program...")


    console_text = read_text_from_console()
    print_text_to_console(f"Console Input: {console_text}")
    write_text_to_file("data/console_output.txt", console_text)


    file_text = read_text_from_file("data/sample.txt")
    print_text_to_console(f"File Input (built-in): {file_text}")
    write_text_to_file("data/file_output.txt", file_text)


    pandas_text = read_text_from_file_with_pandas("data/sample.csv")
    print_text_to_console(f"File Input (pandas): {pandas_text}")
    write_text_to_file("data/pandas_output.txt", pandas_text)

if __name__ == "__main__":
    main()
