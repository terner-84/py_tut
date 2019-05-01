import terner_modules

neco = terner_modules.Experimental(4, 12)

hister = neco.product_of_x()

counter = 0
bla = list()
for i in hister:
    bla.append(i)

print(len(bla))
