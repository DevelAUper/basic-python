# At least 1 letter between [a-z] and 1 letter between [A-Z]. You can use the methods a.islower() and a.isupper() to check if the letter a is one of these.
# At least 1 number between [0-9]. You can use the method a.isnumeric() for this.
# At least 1 character from [$#@]; (a in "$#@" will test if a is one of these).
# Minimum length 6 characters.
# Maximum length 16 characters.
# The program in src/password.py is set up and ready to go, but you need to implement the password checks for it.

import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

for ch in password:
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "$#@" for c in password)
    is_valid = (
        6 <= len(password) <= 16
        and has_lower
        and has_upper
        and has_digit
        and has_special
    )
    break

print(is_valid)
