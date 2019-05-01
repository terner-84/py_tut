import string
import random
import collections
import operator
import terner_modules

print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.hexdigits)



jmena = set()
slovnik = dict()
for x in range(0, 100):
    jmeno = ""
    for y in range(0, random.randint(2, 10)):
        pismeno = random.choice(string.ascii_letters)
        jmeno += pismeno
    jmena.add(jmeno)
    slovnik[jmeno] = random.randint(1928, 1986)

sorted_x = sorted(slovnik.items(), key=operator.itemgetter(0))

sorted_slovnik = collections.OrderedDict(slovnik)

print(type(sorted_slovnik))

for key, value in slovnik.items():
    print(key, value)

