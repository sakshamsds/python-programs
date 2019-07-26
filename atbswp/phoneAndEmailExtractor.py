# Phone and email detection
import re, pyperclip

# sample text
text = '''
dsfadf 870-864-7190 brjones@southark.edu
fadf fadhf x123 870-865-7190 sjordan@southark.edu
fhajdfhkj 2yh 23h hs g98a0 yh 870-864-7122 baaron@southark.edu
'''

# Create a regex for phone number
phoneRegex = re.compile('''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 1234, x12345

(
((\d\d\d) | (\(\d\d\d\)))?    # area code(optional)
(\s|-)    # first separator
\d\d\d    # first 3 digits
-    # second separator
\d\d\d\d    # last 4 digits
(((ext(\.)?\s) | x)    # extension word-part(optional) 
 (\d{2, 5}))?      # extension number-part(optional)
)

''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile('''
# some.+_thing@something.com

[a-zA-Z0-9_.+]+    # name part
@    # @symbol
[a-zA-Z0-9_.+]+    # domain name part

''', re.VERBOSE)

# Get the text off the clipboard
# text = pyperclip.paste()

# Extract email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])          # extracting only the first group which is full phone number

print(allPhoneNumbers)
print(extractedEmail)

# Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) +'\n'+ '\n'.join(extractedEmail)
pyperclip.copy(results)
print(results)
