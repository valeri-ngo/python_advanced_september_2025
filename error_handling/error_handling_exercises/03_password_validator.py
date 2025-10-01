class PasswordTooShortError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
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
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if password_too_common(command, SPECIAL_SYMBOLS):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any(ch in SPECIAL_SYMBOLS for ch in command):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if " " in command:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

print("Password is valid")