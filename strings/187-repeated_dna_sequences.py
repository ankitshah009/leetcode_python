#187. Repeated DNA Sequences
#Medium
#
#The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C',
#'G', and 'T'.
#
#When studying DNA, it is useful to identify repeated sequences within the DNA.
#
#Given a string s that represents a DNA sequence, return all the 10-letter-long
#sequences (substrings) that occur more than once in a DNA molecule. You may
#return the answer in any order.
#
#Example 1:
#Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
#Output: ["AAAAACCCCC","CCCCCAAAAA"]
#
#Example 2:
#Input: s = "AAAAAAAAAAAAA"
#Output: ["AAAAAAAAAA"]
#
#Constraints:
#    1 <= s.length <= 10^5
#    s[i] is either 'A', 'C', 'G', or 'T'.

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []

        seen = set()
        repeated = set()

        for i in range(len(s) - 9):
            seq = s[i:i+10]
            if seq in seen:
                repeated.add(seq)
            seen.add(seq)

        return list(repeated)

    # Rolling hash approach (Rabin-Karp)
    def findRepeatedDnaSequencesRollingHash(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []

        # Map nucleotides to 2-bit values
        char_to_val = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

        # Compute initial hash for first 10 characters
        hash_val = 0
        for i in range(10):
            hash_val = (hash_val << 2) | char_to_val[s[i]]

        seen = {hash_val}
        repeated = set()

        # Mask to keep only 20 bits (10 chars * 2 bits)
        mask = (1 << 20) - 1

        for i in range(10, len(s)):
            # Rolling hash: remove leftmost char, add new char
            hash_val = ((hash_val << 2) | char_to_val[s[i]]) & mask

            if hash_val in seen:
                repeated.add(s[i-9:i+1])
            seen.add(hash_val)

        return list(repeated)
