class NameTooShortError(Exception):
    """Raised when the name length is too short"""
    pass
class MustContainAtSymbolError(Exception):
    """Raised when no special character is present"""
    pass
class InvalidDomainError(Exception):
    """Raised when incorrect domain is entered"""
    pass

MINIMUM_NAME_LENGTH = 5
VALID_DOMAINS = (".com", ".bg", ".org", ".net")

while True:
    email = input()

    if email == 'End':
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if len(email.split("@")[0]) <= MINIMUM_NAME_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = email.split('.')[-1]
    if f".{domain}" not in VALID_DOMAINS:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    print(f"Email is valid")
