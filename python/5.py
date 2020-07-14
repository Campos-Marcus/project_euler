'''2520 is the smallest number that can be divided by each of the 
numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
 divisible by all of the numbers from 1 to 20?

'''


list_aux = []


for n in range(1,500000000):

	if  (n%20 == 0) and (n%19==0) and (n%18 ==0) and (n%17 ==0) and (n%16 ==0) and (n%15 ==0) and (n%14 ==0) and (n%13 ==0) and (n%12 ==0) and (n%11 ==0) and (n%10 == 0) and (n%9==0) and (n%8 ==0) and (n%7 ==0) and (n%6 ==0) and (n%5 ==0) and (n%4 ==0) and (n%3 ==0) and (n%2 ==0) and (n%1 ==0):
		list_aux.append(n)

print(list_aux)

#Ps: takes a while to process


