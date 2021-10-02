print ("Hello world!")
a = int (input ("Целое десятичное число: "))
m = int (a % 10)
b = 0
while a > 0:
	b = int(a % 10)
	if(b % 2 != 0):
		if(m == 0):
			m = b
		else:
			if (b < m):
				m = b 
	a = int(a / 10)
if ( m % 2 == 0):
	print("Число не содержит четных цифр")
else: 
	print (m)
