#192. Word Frequency
#Medium
#
#Write a bash script to calculate the frequency of each word in a text file
#words.txt.
#
#For simplicity sake, you may assume:
#    words.txt contains only lowercase characters and space ' ' characters.
#    Each word must consist of lowercase characters only.
#    Words are separated by one or more whitespace characters.
#
#Example:
#Assume that words.txt has the following content:
#the day is sunny the the
#the sunny is is
#
#Your script should output the following, sorted by descending frequency:
#the 4
#is 3
#sunny 2
#day 1
#
#Note:
#Don't worry about handling ties, it is guaranteed that each word's frequency
#count is unique.

# Bash Solution 1: Using tr, sort, uniq
"""
#!/bin/bash
cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -rn | awk '{print $2, $1}'
"""

# Bash Solution 2: Using awk
"""
#!/bin/bash
awk '{
    for (i = 1; i <= NF; i++) {
        count[$i]++
    }
}
END {
    for (word in count) {
        print word, count[word]
    }
}' words.txt | sort -k2 -rn
"""

# Bash Solution 3: Using xargs
"""
#!/bin/bash
cat words.txt | xargs -n 1 | sort | uniq -c | sort -rn | awk '{print $2, $1}'
"""

# Python equivalent for reference:
def word_frequency(filename: str) -> list:
    """Python equivalent of the bash solution"""
    from collections import Counter

    with open(filename, 'r') as f:
        words = f.read().split()

    counter = Counter(words)

    # Sort by frequency descending
    sorted_words = sorted(counter.items(), key=lambda x: -x[1])

    return [(word, count) for word, count in sorted_words]


# One-liner Python:
def word_frequency_oneliner(filename: str) -> list:
    from collections import Counter
    return sorted(Counter(open(filename).read().split()).items(), key=lambda x: -x[1])
