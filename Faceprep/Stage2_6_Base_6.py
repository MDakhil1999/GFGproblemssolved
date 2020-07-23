# Base 6
# Given a sequence of distinct numbers a1, a2, ….. an, an inversion occurs if there are indices i aj . For example, in the sequence 2 1 4 3 there are 2 inversions (2 1) and (4 3). The input will be a main sequence of N positive integers. From this sequence, a Derived Sequence will be obtained using the following rule. The output is the number of inversions in the derived sequence.

# Rule for forming derived sequence

# An integer may be represented in base 6 notation. In base 6, 10305 is 1x64 + 3x62 + 5 =1409. Note that none of the digits in that representation will be more than 5.

# The sum of digits in a base 6 representation is the sum of all the digits at the various positions in the representation. Thus for the number 1409, the representation is 10305, and the sum of digits is 1+0+3+0+5=9. The sum of digits may be done in the decimal system, and does not need to be in base 6. The derived sequence is the sum of the digits when the corresponding integer is represented in the base 6 form number will be expressed in base 6, and the derived sequence is the sum of the digits of the number in the base 6 representation.

# Input Format

# The first line of the input will have a single integer, which will give N.

# The next line will consist of a comma separated string of N integers, which is the main sequence

# Output Format

# The number of inversions in the derived sequence formed from the main sequence.

# Constraints

# N <= 50

# Integers in sequence <= 107

# Refer the sample output for formatting

# Sample Input

# 5

# 55 53 88 27 33

# Sample Output

# 2






n = int(input())
arr = list(map(int,input().split()))
matrix = []
for i in arr:
    hai = []
    while i != 0:
        hai.append(i%6)
        i = i//6
    hai = hai[::-1]
    matrix.append(sum(hai))
inversions = 0
for i in range(0,n-1):
    for j in range(i+1,n):
        if matrix[i] > matrix[j]:
            inversions += 1
print(inversions)

    