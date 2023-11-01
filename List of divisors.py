n = int(input("enter a number:  ")) 
TAB=[]
div_count=0
for i in range(n,0,-1):
 if n%i==0:
  div_count+=1
  TAB.append(i)
print(f"the divisors counts is {div_count} and the list of divisors is {TAB}")