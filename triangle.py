wing1 = int(input())
wing2 = int(input())
wing3 = int(input())
A = wing1 < wing2 + wing3
B = wing2 < wing3 + wing1
C = wing3 < wing1 + wing2
print(A)
print(B)
print(C)


