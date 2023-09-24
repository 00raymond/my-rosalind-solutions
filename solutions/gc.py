#split dataset into arr via ">"
#split elements further by end lines

with open('rosalind_gc.txt', 'r') as f:
    contents = f.read()

c = contents.split(">")

curmax = 0
curmaxid = ""

for item in c:
    if not item:
        continue

    id = item.split('\n', 1)[0]
    seq = item.split('\n', 1)[1].replace('\n', '')
    gcount = item.count('G')
    ccount = item.count('C')

    gc = ((gcount + ccount) / len(seq)) * 100
    if gc > curmax:
        curmax = gc
        curmaxid = id

print(curmaxid)
print(curmax)