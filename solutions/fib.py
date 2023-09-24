def fib(month, pairs):
    if month <= 2:
        return 1
    else:
        return fib(month - 1, pairs) + pairs * fib(month - 2, pairs)


with open('rosalind_fib.txt', 'r') as f:
    contents = f.read()

c = contents.split()

mo = int(c[0])
rp = int(c[1])

np = fib(mo, rp)

print(np)
