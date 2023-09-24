with open('rosalind_hamm.txt', 'r') as f:
    contents = f.read()

c = contents.split('\n')
s1 = c[0]
print(s1)
s2 = c[1]
print(s2)

hamming_dist = 0

count = ()
for char1, char2 in zip(s1, s2):
    if char1 != char2:
        hamming_dist += 1

print(hamming_dist)
