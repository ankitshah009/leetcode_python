#193. Valid Phone Numbers
#Easy
#
#Given a text file file.txt that contains a list of phone numbers (one per line),
#write a one-liner bash script to print all valid phone numbers.
#
#You may assume that a valid phone number must appear in one of the following
#two formats:
#    (xxx) xxx-xxxx
#    xxx-xxx-xxxx
#(x means a digit)
#
#You may also assume each line in the text file must not contain leading or
#trailing white spaces.
#
#Example:
#Assume that file.txt has the following content:
#987-123-4567
#123 456 7890
#(123) 456-7890
#
#Your script should output the following valid phone numbers:
#987-123-4567
#(123) 456-7890

# Bash Solution 1: Using grep with extended regex
"""
#!/bin/bash
grep -E '^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$' file.txt
"""

# Bash Solution 2: Using awk
"""
#!/bin/bash
awk '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/' file.txt
"""

# Bash Solution 3: Using sed
"""
#!/bin/bash
sed -n -E '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/p' file.txt
"""

# Python equivalent for reference:
import re

def valid_phone_numbers(filename: str) -> list:
    """Python equivalent of the bash solution"""
    pattern = r'^(\(\d{3}\) |\d{3}-)\d{3}-\d{4}$'

    valid_numbers = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if re.match(pattern, line):
                valid_numbers.append(line)

    return valid_numbers


def valid_phone_numbers_oneliner(filename: str) -> list:
    """One-liner Python solution"""
    import re
    return [l.strip() for l in open(filename) if re.match(r'^(\(\d{3}\) |\d{3}-)\d{3}-\d{4}$', l.strip())]
