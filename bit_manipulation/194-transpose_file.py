#194. Transpose File
#Medium
#
#Given a text file file.txt, transpose its content.
#
#You may assume that each row has the same number of columns, and each field
#is separated by the ' ' character.
#
#Example:
#If file.txt has the following content:
#name age
#alice 21
#ryan 30
#
#Output the following:
#name alice ryan
#age 21 30

# Bash Solution 1: Using awk
"""
#!/bin/bash
awk '{
    for (i = 1; i <= NF; i++) {
        if (NR == 1) {
            row[i] = $i
        } else {
            row[i] = row[i] " " $i
        }
    }
}
END {
    for (i = 1; i <= NF; i++) {
        print row[i]
    }
}' file.txt
"""

# Bash Solution 2: Using multiple passes
"""
#!/bin/bash
ncol=$(head -1 file.txt | wc -w)
for i in $(seq 1 $ncol); do
    awk -v col=$i '{printf "%s%s", (NR==1?"":OFS), $col} END{print ""}' file.txt
done
"""

# Bash Solution 3: Using cut and paste
"""
#!/bin/bash
ncol=$(head -1 file.txt | wc -w)
for i in $(seq 1 $ncol); do
    cut -d' ' -f$i file.txt | paste -sd' '
done
"""

# Python equivalent for reference:
def transpose_file(filename: str) -> list:
    """Python equivalent of the bash solution"""
    with open(filename, 'r') as f:
        lines = [line.strip().split() for line in f]

    if not lines:
        return []

    # Transpose using zip
    transposed = list(zip(*lines))

    return [' '.join(row) for row in transposed]


def transpose_file_numpy(filename: str) -> list:
    """Using numpy for transposition"""
    import numpy as np
    with open(filename, 'r') as f:
        matrix = [line.strip().split() for line in f]
    transposed = np.array(matrix).T
    return [' '.join(row) for row in transposed]
