# Password-Strength-Checker
CS50P Final Project: A Python tool that analyzes password strength and suggests security improvements.
# Password Strength Checker

#### Video Demo:  <INSERT YOUR YOUTUBE VIDEO LINK HERE>

#### Description:
The **Password Strength Checker** is a command-line interface (CLI) tool written in Python that evaluates the security strength of a user-provided password. Instead of simply accepting or rejecting a password, this tool calculates a "security score" and provides specific, actionable feedback on how to improve the password.

This project was built to address the real-world problem of weak account security. By using **Regular Expressions (Regex)**, the program efficiently scans strings for specific patterns (digits, special characters, uppercase letters) to ensure users meet modern security standards.

### Project Structure

 The project consists of the following files:

- **`project.py`**: This is the main script containing the logic.
    - `main()`: Handles user input and displays the final score and feedback.
    - `check_password(password)`: The core controller function. It runs the password through four specific checks and returns a tuple containing the integer score (0-4) and a list of feedback strings.

    - **Helper Functions**:
        - `has_good_length(pw)`: Checks if the password is at least 8 characters long.
        - `has_number(pw)`: Uses Regex to find digits.
        - `has_upper(pw)`: Uses Regex to find uppercase letters.
        - `has_special(pw)`: Uses Regex to find special characters (e.g., @, #, $).

- **`test_project.py`**: Contains unit tests for `project.py` using the `pytest` framework.
    - It verifies that the helper functions correctly identify valid and invalid inputs.
    - It ensures the `check_password` logic calculates the correct score for mixed-case scenarios.

- **`requirements.txt`**: Lists the external libraries required to run the tests (specifically `pytest`).

### Design Choices

#### 1. Regular Expressions (`re` library)
I chose to use Python's built-in `re` library instead of looping through each character of the string manually. Using `re.search` is more readable and computationally efficient for pattern matching.

#### 2. Boolean Type Casting
In the helper functions (e.g., `has_number`), I wrapped the Regex search in `bool()`.
```python
return bool(re.search(r"\d", pw))
