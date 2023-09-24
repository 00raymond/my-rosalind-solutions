
with open('rosalind_revc.txt', 'r') as f:
    contents = f.read()

seq = contents[::-1]

seq = seq.replace("C", "temp")
seq = seq.replace("G", "C")
seq = seq.replace("temp", "G")

seq = seq.replace("A", "temp")
seq = seq.replace("T", "A")
seq = seq.replace("temp", "T")

print(seq)