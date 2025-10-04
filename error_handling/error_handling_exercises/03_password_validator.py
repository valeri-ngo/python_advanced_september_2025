class PasswordTooShortError(Exception):
    """Raised when the password length is too short"""
    pass

class PasswordTooCommonError(Exception):
    """
    Raised when the current password contains only
    letters, numbers or special characters"""
    pass

class PasswordNoSpecialCharactersError(Exception):
    """Raised when there is no special character entered"""
    pass

class PasswordContainsSpacesError(Exception):
    """Raised when password contains a blank space"""
    pass

def password_too_common(pwd, special_char):
    only_digits = pwd.isdigit()
    only_letters = pwd.isalpha()
    only_specials = all(ch in special_char for ch in pwd)
    return only_letters or only_digits or only_specials

SPECIAL_SYMBOLS = ("@", "*", "&", "%")

while True:
    command = input()

    if command == "Done":
        break

    if len(command) < 8:
        # Checks if password is long enough
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if password_too_common(command, SPECIAL_SYMBOLS):
        # Checks if password contains only letters, digits or special characters
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any(ch in SPECIAL_SYMBOLS for ch in command):
        # Checks if special character is entered or not
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if " " in command:
        # Checks if there is a blank space present
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

print("Password is valid")