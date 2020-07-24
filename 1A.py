x=input('').split()
n,m,a=[int(i) for  i in x]
if((n % a)==0): n = n // a;
else:n = n // a + 1
if((m % a)==0): m = m // a;
else:m = m // a + 1;
print(n * m )
