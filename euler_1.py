sum=0
for i in range(3,1000):
	if(i%3==0 or i%5==0):
		sum+=i
print("Sum of divisors(3 5) below 1000 is",sum)