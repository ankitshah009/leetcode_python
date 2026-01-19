#195. Tenth Line
#Easy
#
#Given a text file file.txt, print just the 10th line of the file.
#
#Example:
#Assume that file.txt has the following content:
#Line 1
#Line 2
#Line 3
#Line 4
#Line 5
#Line 6
#Line 7
#Line 8
#Line 9
#Line 10
#
#Your script should output the tenth line, which is:
#Line 10
#
#Note:
#1. If the file contains less than 10 lines, what should you output?
#2. There's at least three different solutions. Try to explore all possibilities.

# Bash Solution 1: Using sed
"""
#!/bin/bash
sed -n '10p' file.txt
"""

# Bash Solution 2: Using awk
"""
#!/bin/bash
awk 'NR == 10' file.txt
"""

# Bash Solution 3: Using head and tail
"""
#!/bin/bash
head -10 file.txt | tail -1
"""

# Bash Solution 4: Using tail with check
"""
#!/bin/bash
line_count=$(wc -l < file.txt)
if [ $line_count -ge 10 ]; then
    tail -n +10 file.txt | head -1
fi
"""

# Bash Solution 5: Using mapfile/readarray
"""
#!/bin/bash
mapfile -t lines < file.txt
if [ ${#lines[@]} -ge 10 ]; then
    echo "${lines[9]}"
fi
"""

# Python equivalent for reference:
def tenth_line(filename: str) -> str:
    """Python equivalent of the bash solution"""
    with open(filename, 'r') as f:
        for i, line in enumerate(f, 1):
            if i == 10:
                return line.strip()
    return ""  # File has less than 10 lines


def tenth_line_readlines(filename: str) -> str:
    """Using readlines"""
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines[9].strip() if len(lines) >= 10 else ""
