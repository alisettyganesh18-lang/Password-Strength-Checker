import re

def main():
    print("🔒 PASSWORD STRENGTH CHECKER 🔒")

    while True:
        password = input("\nEnter a password to test: ") 
        score, feedback = check_password(password)

        print(f"Final Score: {score}/4")

        if score == 4:
            print("✅ Strong Password! (Great job)")
            break  # This exits the loop
        else:
            print("⚠️ Weak Password. Here is how to fix it:")
            for tip in feedback:
                print(f" - {tip}")
            print("\nPlease try again to reach a 4/4 score.")

    print("\nProgram finished. Your account is secure!")


def check_password(password):
    """
    Analyzes the password and returns a tuple: (score, feedback_list)
    """
    score = 0
    feedback = []

    # Check 1: Length
    if has_good_length(password):
        score += 1
    else:
        feedback.append("Too short (needs 8+ characters)")

    # Check 2: Numbers
    if has_number(password):
        score += 1
    else:
        feedback.append("Missing a number")

    # Check 3: Uppercase
    if has_upper(password):
        score += 1
    else:
        feedback.append("Missing an uppercase letter")

    # Check 4: Special Characters
    if has_special(password):
        score += 1
    else:
        feedback.append("Missing a special character (@, #, $, etc.)")

    return score, feedback


# --- Helper Functions ---

def has_good_length(pw):
    """Returns True if password is at least 8 characters long."""
    return len(pw) >= 8


def has_number(pw):
    """Returns True if password contains at least one digit."""
    # \d looks for any digit 0-9
    return bool(re.search(r"\d", pw))


def has_upper(pw):
    """Returns True if password contains at least one uppercase letter."""
    # [A-Z] looks for any uppercase letter
    return bool(re.search(r"[A-Z]", pw))


def has_special(pw):
    """Returns True if password contains at least one special character."""
    # The string inside [] lists the allowed special characters
    # We escape special regex characters like . or * with a backslash if needed,
    # but inside [] most are treated literally.
    return bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", pw))


if __name__ == "__main__":
    main()
