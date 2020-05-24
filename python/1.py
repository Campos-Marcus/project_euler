sum_list = []
aux = 0

for n in range(1,1000):
    if (n%5 == 0) or (n%3 == 0):
        sum_list.append(n)
    
for n in sum_list:
    aux += n
print(aux)


