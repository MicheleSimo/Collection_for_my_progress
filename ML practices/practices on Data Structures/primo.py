import random
import string

lol1 = "kldogkdr"
print(lol1.upper())
lol2 = [char for char in lol1]
print(lol2)
lol4 = "olowekpfprg"
lol3 = lol4.split()
print(lol4)

#generazione random
print(string.ascii_letters)
print(string.digits)
newRandomString = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(11))
print(newRandomString)
arrayNumbers = [c for c in newRandomString if c.isdigit()]
countNumber = len(arrayNumbers)
print(countNumber)
