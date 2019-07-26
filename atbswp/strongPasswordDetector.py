import re

passwordRegex = re.compile(r'''(
    ^(?=.*[A-Z])                # at least one capital letter
    (?=.*[!@#$&*])                     # at least one of these special characters
    (?=.*[0-9])                 # at least one numeric digit
    (?=.*[a-z])          # at least one lower case letter
    .{8,}                              # at least 8 total digits
    $
    )''', re.VERBOSE)

def userInputPasswordCheck():
    ppass = input("Enter a potential password: ")
    mo = passwordRegex.search(ppass)
    if (not mo):
        print("Doesn't meet the requirement")
        return False
    else:
        print("Meets the requirement, Enjoy")
        return True


userInputPasswordCheck()
