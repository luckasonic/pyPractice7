
import unittest
from app.io.input import read_text_from_file, read_text_from_file_with_pandas
import pandas as pd
import os

class TestInputFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Create test files before running tests."""
        os.makedirs("data", exist_ok=True)
        with open("data/test_file.txt", "w") as f:
            f.write("Hello, world!")
        pd.DataFrame({"name": ["Alice", "Bob"], "age": [30, 25]}).to_csv("data/test_file.csv", index=False)

    @classmethod
    def tearDownClass(cls):
        """Clean up test files after running tests."""
        try:
            os.remove("data/test_file.txt")
            os.remove("data/test_file.csv")
        except Exception as e:
            print(f"Error during cleanup: {e}")

    def test_read_text_from_file_valid(self):
        """Test reading from an existing file."""
        result = read_text_from_file("data/test_file.txt")
        self.assertEqual(result, "Hello, world!")

    def test_read_text_from_file_nonexistent(self):
        """Test reading from a non-existent file."""
        result = read_text_from_file("data/nonexistent.txt")
        self.assertEqual(result, "File not found: data/nonexistent.txt")

    def test_read_text_from_empty_file(self):
        """Test reading from an empty file."""
        open("data/empty.txt", "w").close()
        result = read_text_from_file("data/empty.txt")
        self.assertEqual(result, "")
        os.remove("data/empty.txt")

    def test_read_text_from_file_with_pandas_valid(self):
        """Test reading a CSV file using pandas."""
        result = read_text_from_file_with_pandas("data/test_file.csv")
        expected = '    name  age\n0  Alice   30\n1    Bob   25'
        self.assertIn(expected, result)

    def test_read_text_from_file_with_pandas_nonexistent(self):
        """Test reading a non-existent file with pandas."""
        result = read_text_from_file_with_pandas("data/nonexistent.csv")
        self.assertEqual(result, "File not found: data/nonexistent.csv")

    def test_read_text_from_file_with_pandas_empty(self):
        """Test reading an empty CSV file with pandas."""
        open("data/empty.csv", "w").close()
        result = read_text_from_file_with_pandas("data/empty.csv")
        self.assertEqual(result, "File is empty: data/empty.csv")
        os.remove("data/empty.csv")

if __name__ == "__main__":
    unittest.main()
