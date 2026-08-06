def find_lcs(text1, text2):
    rows = len(text1)
    cols = len(text2)

    # Create DP table
    table = [[0] * (cols + 1) for _ in range(rows + 1)]

    # Fill DP table
    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            if text1[row - 1] == text2[col - 1]:
                table[row][col] = table[row - 1][col - 1] + 1
            else:
                table[row][col] = max(table[row - 1][col], table[row][col - 1])

    # Backtrack to find LCS
    row = rows
    col = cols
    lcs_chars = []

    while row > 0 and col > 0:
        if text1[row - 1] == text2[col - 1]:
            lcs_chars.append(text1[row - 1])
            row -= 1
            col -= 1
        elif table[row - 1][col] > table[row][col - 1]:
            row -= 1
        else:
            col -= 1

    lcs_chars.reverse()

    return "".join(lcs_chars), table[rows][cols]


# Main Program
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

subsequence, lcs_length = find_lcs(string1, string2)

print("\nLongest Common Subsequence:", subsequence)
print("Length of LCS:", lcs_length)

'''
OUTPUT:
Enter first string: ABCDGH
Enter second string: AEDFHR

Longest Common Subsequence: ADH
Length of LCS: 3
'''
